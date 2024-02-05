from fastapi import APIRouter
from src.auth.models import UserLogin, User
from fastapi import Body
from src.auth.utils import check_user, signJWT, hash_password
from src.database import add_user, get_user

users = []

login_router = APIRouter(prefix="/auth")
@login_router.post("/login")
async def login(user: UserLogin = Body(...)):
    response = get_user(user)
    return response



@login_router.post("/signup")
def create_user(user: User = Body(...)):
    user.password = hash_password(user.password)
    add_user(user)# replace with db call, making sure to hash the password first
    return signJWT(user.email)


@login_router.post("/logout")
async def logout():
    return {"message": "Hello World"}


@login_router.post("/forgot-password")
async def forgot_password():
    return {"message": "Hello World"}


@login_router.post("/reset-password")
async def reset_password():
    return {"message": "Hello World"}


@login_router.post("/change-password")
async def change_password():
    return {"message": "Hello World"}
