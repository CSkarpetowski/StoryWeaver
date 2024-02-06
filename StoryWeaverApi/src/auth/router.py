from fastapi import APIRouter, Depends
from fastapi import Body

import src.database as db
from src.auth.dependencies import JWTBearer
from src.auth.models import UserLogin, User
from src.auth.utils import check_user, signJWT, hash_password

users = []

login_router = APIRouter(prefix="/auth")
auth_router = APIRouter(prefix="/authorized")
login_router.include_router(auth_router)


def is_jwtup(user: UserLogin):
    return check_user(user, users)


@login_router.post("/login")
async def login(user: UserLogin = Body(...)):
    response = db.get_user(user)
    if response:
        return signJWT(user.email)
    else:
        return {"error": "Invalid credentials"}


@login_router.post("/signup")
def create_user(user: User = Body(...)):
    user.password = hash_password(user.password)
    response = db.add_user(user)  # replace with db call, making sure to hash the password first
    if response:
        return {"message": "User created"}
    else:
        return {"error": "User already exists"}


@login_router.post("/forgot-password")
async def forgot_password():
    return {"message": "Hello World"}


@auth_router.post("/logout{email}", dependencies=[Depends(JWTBearer)])
async def logout(email: str):
    try:
        db.delete_user(email)
        return {"message": "User deleted"}
    except Exception as e:
        print(e)
        return {"message": "User not found"}


@auth_router.post("/reset-password", dependencies=[Depends(JWTBearer)])
async def reset_password():
    return {"message": "Hello World"}


@auth_router.post("/change-password", dependencies=[Depends(JWTBearer)])
async def change_password():
    return {"message": "Hello World"}

