from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# Mongo DB connection
mongo_client = MongoClient("mongodb://admin_user:web3@localhost:27017/")
database = mongo_client["web3"]
productos_collection = database["productos"]

@app.get("/")
def DBStart():
    return{"status": "started"}

@app.get("/health")
def health_check():
    return{"status": "ok"}


@app.get("/productos")
def get_productos():
    return list(productos_collection.find({}, {"_id": 0}))

