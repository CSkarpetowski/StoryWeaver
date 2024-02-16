from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Body, BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm

import src.database as db
from src.auth.Email.models import EmailSchema
from src.auth.JWT.utils import sign_jwt, generate_password_authenticate_token, decode_jwt
from src.auth.dependencies import oauth2
from src.auth.models import UserLogin, User, ResetPassword, EmailForReset
from src.auth.utils import hash_password
from src.auth.Email.utils import send_email


login_router = APIRouter(prefix="/auth")
auth_router = APIRouter(prefix="/authorized")
login_router.include_router(auth_router)


@login_router.post("/login", status_code=200)
async def login(user: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_from_form = UserLogin(username=user.username, password=user.password)
    response = db.get_user(user_from_form)
    if response:
        return sign_jwt(user.username)
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")


@login_router.post("/signup", status_code=201)
def create_user(backgroundtask: BackgroundTasks, user: User = Body(...)):
    user.password = hash_password(user.password)
    response = db.add_user(user)  # replace with db call, making sure to hash the password first
    activation_token = generate_password_authenticate_token(user.email)
    print(activation_token)
    user.activation_token = activation_token
    db.update_user(user.email, {"activation_token": activation_token})
    recipient = EmailSchema(email=user.email, subject="Activate your account")
    context = {
        "username": user.username,
        "token": activation_token
    }
    backgroundtask.add_task(send_email, recipient, "confirmation_mail_template.html", context)
    if response:
        return "Singed up successfully"
    else:
        raise HTTPException(status_code=400, detail="User already exists")


@auth_router.get("/activate/{token}", status_code=200)
def activate_account(token: str):
    token_decoded = decode_jwt(token)
    if token_decoded:
        db.update_user(token_decoded["sub"], {"active": True})
        return {"message": "Account activated"}
    else:
        raise HTTPException(status_code=400, detail="Invalid token or expired token")


@auth_router.post("/reset-password", status_code=200)
async def reset_password(backgroundtask: BackgroundTasks, email: EmailForReset = Body(...)):
    user = db.get_user_by_email(email.email)
    if user:
        reset_token = generate_password_authenticate_token(email.email)
        db.update_user(email.email, {"reset_token": reset_token})
        recipient = EmailSchema(email=email.email, subject="Reset your password")
        context = {
            "username": user["username"],
            "token": reset_token
        }
        backgroundtask.add_task(send_email, recipient, "reset_password_mail_template.html", context)
        return {"message": "Reset password email sent"}
    else:
        raise HTTPException(status_code=404, detail="User not found")


@auth_router.post("/change-password/{token}", status_code=200)
async def change_password(token: str, reset: ResetPassword = Body(...)):
    token_decoded = decode_jwt(token)
    if token_decoded:
        user = db.get_user_by_email(token_decoded["sub"])
        if user and user["reset_token"] == token:  # access reset_token as a key in the user dictionary
            new_password = hash_password(reset.password)
            db.update_user(token_decoded["sub"], {"password": new_password, "reset_token": None})
            return {"message": "Password changed successfully"}
        else:
            raise HTTPException(status_code=400, detail="Invalid token or expired token")
    else:
        raise HTTPException(status_code=400, detail="Invalid token or expired token")


@auth_router.delete("/delete-account/{email}", dependencies=[Depends(oauth2)], status_code=204)
def delete_account(email: str):
    try:
        db.delete_user(email)
        return {"message": "User deleted"}
    except Exception as e:
        print(e)
        return {"message": "User not found"}
