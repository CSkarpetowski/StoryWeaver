from pydantic import BaseModel, Field


class Story(BaseModel):
    creator: str = Field(default=None)
    story: str = Field(default=None)
    tags: list = Field(default=None)
    user: str = Field(default=None)

    class Config:
        json_schema_extra = {
            "example": {
                "creator": "Joe Doe",
                "story": "Once upon a time...",
                "tags": ["adventure", "fantasy"],
                "user": "userid"
            }
        }
