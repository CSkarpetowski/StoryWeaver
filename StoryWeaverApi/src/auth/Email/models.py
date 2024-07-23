from pydantic import BaseModel, Field, EmailStr
from pydantic.functional_validators import field_validator


class EmailSchema(BaseModel):
    email: EmailStr = Field(default=None)
    subject: str = Field(default=None)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "test@test.com",
                "subject": "Test Subject"
                }
            }


@field_validator('email')
def validate_email(cls, v):
    if not v:
        return v
