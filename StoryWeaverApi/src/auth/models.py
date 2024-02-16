from pydantic import BaseModel, Field, EmailStr
from pydantic.functional_validators import field_validator


class User(BaseModel):
    username: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    active: bool = Field(default=False)
    activation_token: str = Field(default=None)


    @field_validator("username")
    @classmethod
    def username_validator(cls, v: str) -> str:
        if len(v) < 5:
            raise ValueError("Username must be at least 5 characters long")
        return v

    class Config:
        json_schema_extra = {
            "example": {
                "username": "Joe Doe",
                "email": "joe@xyz.com",
                "password": "any"
            }
        }


class UserLogin(BaseModel):
    username: str = Field(default=None)
    password: str = Field(default=None)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "Joe Doe",
                "password": "any"
            }
        }
