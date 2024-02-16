from decouple import config
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from pymongo.mongo_client import MongoClient
from fastapi.middleware.cors import CORSMiddleware
from src.auth.dependencies import JWTBearer
from src.auth.router import login_router, auth_router
from src.chatbot.router import chatbot_router

load_dotenv()

uri = config('MONGODB_URI')

# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection


app = FastAPI()
app.include_router(login_router)
app.include_router(auth_router)
app.include_router(chatbot_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}", dependencies=[Depends(JWTBearer)])
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




