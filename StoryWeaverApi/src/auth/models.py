from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    username: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        schema_extra = {
            "example": {
                "username": "Joe Doe",
                "email": "joe@xyz.com",
                "password": "any"
            }
        }


class UserLogin(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        schema_extra = {
            "example": {
                "email": "joe@xyz.com",
                "password": "any"
            }
        }
