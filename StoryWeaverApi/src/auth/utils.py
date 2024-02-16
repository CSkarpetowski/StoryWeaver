
from passlib.context import CryptContext

from .models import User, UserLogin


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def check_user(data: UserLogin, users: list[User]):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)
