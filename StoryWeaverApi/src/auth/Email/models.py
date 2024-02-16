from pydantic import BaseModel, Field, EmailStr
from pydantic.functional_validators import field_validator


class EmailSchema(BaseModel):
    email: EmailStr = Field(default=None)
    subject: str = Field(default=None)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "test@test.com",
                "subject": "Test Subject",
                "link": "any",
                "username": "TestUser"
                }
            }