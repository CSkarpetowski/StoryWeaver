from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
from decouple import config
from src.auth.router import login_router

load_dotenv()

mongopass = config('MONGODB_PASSWORD')

uri = f"mongodb+srv://root:{mongopass}@storyweaver.l1fjbdq.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection



app = FastAPI()
app.include_router(login_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/db")
async def db():
    print(uri)
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return {"message": "Pinged your deployment. You successfully connected to MongoDB!"}
    except Exception as e:
        print(e)
        return {"message": "Failed to connect to MongoDB!"}
