from fastapi import APIRouter, Depends, Body

from src.auth.dependencies import JWTBearer
from src.chatbot.models import Story
import src.database as db

chatbot_router = APIRouter(prefix="/chatbot")


@chatbot_router.post("/story/{email}", dependencies=[Depends(JWTBearer)], tags=["stories"])
def create_story(email, story: Story = Body(...)):
    user = db.get_user_id(email)
    db.add_story(story, user)
