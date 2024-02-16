import time
from typing import Dict

from decouple import config
from fastapi import Depends, Response, Request
from jose import jwt

JWT_SECRET = config('JWT_SECRET')
ALGORITHM = config('JWT_ALGORITHM')


def token_response(token: str):
    return {
        'access_token': token
    }


def sign_jwt(user_id: str) -> Dict[str, str]:
    payload = {
        'user_id': user_id,
        'expires': time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)

    return token_response(token)


def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        return decoded_token if decoded_token["exp"] >= time.time() else None
    except Exception as e:
        print(e)
        return {}


async def check_jwt(request: Request, next_: callable = Depends):
    jwt_check = request.headers.get("Authorization")
    if jwt_check:
        if decode_jwt(jwt_check):
            return await next_(request)
        else:
            return Response("Invalid token or expired token", status_code=403)
    else:
        return Response("Not authorized", status_code=403)


def generate_password_authenticate_token(email: str) -> str:
    payload = {
        "sub": email,
        "exp": time.time() + 600
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)
