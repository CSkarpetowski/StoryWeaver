from pymongo.mongo_client import MongoClient
from decouple import config
from .auth.models import User

uri = config('MONGODB_URI')

# Create a new client and connect to the server
client = MongoClient(uri)

db = client['StoryWeaver']
users = db['Users']

def get_user(email):
    return users.find_one({"email": email})

def add_user(User):
    user_dict = User.dict()
    users.insert_one(user_dict)

def update_user(email, user):
    users.update_one({"email": email}, {"$set": user})

def delete_user(email):
    users.delete_one({"email": email})