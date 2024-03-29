from decouple import config
from pymongo.mongo_client import MongoClient
from src.auth.utils import verify_password

uri = config('MONGODB_URI')

# Create a new client and connect to the server
client = MongoClient(uri)

db = client[config('MONGODB_CLUSTER')]
users = db[config('MONGODB_DATABASE')]
stories = db[config('MONGODB_STORIES_COLLECTION')]


def get_user(user_login):
    user_dict = user_login.dict()
    try:
        user_data = users.find_one({"username": user_dict["username"]})
        if user_data:
            user_dict["password"] = verify_password(user_dict["password"], user_data["password"])
            if user_dict["password"]:
                print("Password verification successful.")
                return True
            else:
                print("Password verification failed.")
                return False
        else:
            print("User not found in the database.")
            return False

    except Exception as e:
        # Handle specific exceptions if needed or print the exception for debugging
        print(f"Error: {e}")
        return False


def get_user_by_email(email):
    return users.find_one({"email": email})


def add_user(user):
    user_dict = user.dict()
    existing_user = users.find_one({"email": user_dict["email"]})
    if existing_user:
        print("User with the same email already exists.")
        return False
    else:
        users.insert_one(user_dict)
        print("User added successfully.")
        return True


def update_user(email, user):
    users.update_one({"email": email}, {"$set": user})


def delete_user(email):
    users.delete_one({"email": email})


def add_story(story, user_id):
    story.user = user_id
    story_dict = story.dict()
    stories.insert_one(story_dict)


def get_user_id(email):
    user = users.find_one({"email": email})
    return user["_id"]
