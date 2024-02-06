import time
from typing import Dict
from jose import jwt
from decouple import config
from fastapi import Depends, Response, Request
from .models import User, UserLogin
import bcrypt
from passlib.context import CryptContext

JWT_SECRET = config('JWT_SECRET')
ALGORITHM = config('JWT_ALGORITHM')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def token_response(token: str):
    return {
        'access_token': token
    }


def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        'user_id': user_id,
        'expires': time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}


def deleteJWT(request: Request):
    token = request.headers.get("Authorization")
    if token:
        token['expires'] = time.time()


def check_user(data: UserLogin, users: list[User]):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


async def check_jwt(request: Request, next_: callable = Depends):
    jwt = request.headers.get("Authorization")
    if jwt:
        if decodeJWT(jwt):
            return await next_(request)
        else:
            return Response("Invalid token or expired token", status_code=403)
    else:
        return Response("Not authorized", status_code=403)
