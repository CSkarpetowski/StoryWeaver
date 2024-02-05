from fastapi import FastAPI
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://root:bwNoWgPXx2fvB7Dy@storyweaver.l1fjbdq.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/db")
async def db():
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return {"message": "Pinged your deployment. You successfully connected to MongoDB!"}
    except Exception as e:
        print(e)
        return {"message": "Failed to connect to MongoDB!"}
