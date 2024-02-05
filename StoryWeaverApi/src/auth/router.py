from fastapi import APIRouter, Depends, Request
from src.auth.models import UserLogin, User
from fastapi import Body
from src.auth.utils import check_user, signJWT, hash_password, deleteJWT, check_jwt
from src.database import add_user, get_user
from src.auth.service import JWTBearer

users = []

login_router = APIRouter(prefix="/auth")
auth_router = APIRouter(prefix="/authorized")
login_router.include_router(auth_router)

def is_jwtup(user: UserLogin):
    return check_user(user, users)


@login_router.post("/login")
async def login(user: UserLogin = Body(...)):
    response = get_user(user)
    return signJWT(user.email)


@login_router.post("/signup")
def create_user(user: User = Body(...)):
    user.password = hash_password(user.password)
    add_user(user)  # replace with db call, making sure to hash the password first
    return "Singed up successfully"


@login_router.post("/forgot-password")
async def forgot_password():
    return {"message": "Hello World"}


@auth_router.post("/logout", dependencies=[Depends(JWTBearer)])
async def logout():

    return {"message": "Hello World"}


@auth_router.post("/reset-password", dependencies=[Depends(JWTBearer)])
async def reset_password():
    return {"message": "Hello World"}


@auth_router.post("/change-password", dependencies=[Depends(JWTBearer)])
async def change_password():
    return {"message": "Hello World"}
