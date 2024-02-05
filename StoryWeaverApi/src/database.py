from decouple import config
from pymongo.mongo_client import MongoClient
from src.auth.utils import verify_password

uri = config('MONGODB_URI')

# Create a new client and connect to the server
client = MongoClient(uri)

db = client['StoryWeaver']
users = db['Users']


def get_user(UserLogin):
    user_dict = UserLogin.dict()
    try:
        user_dict["password"] = verify_password(user_dict["password"],
                                                users.find_one({"email": user_dict["email"]})["password"])
        return user_dict
    except:
        return "User not found"


def add_user(User):
    user_dict = User.dict()
    users.insert_one(user_dict)


def update_user(email, user):
    users.update_one({"email": email}, {"$set": user})


def delete_user(email):
    users.delete_one({"email": email})
