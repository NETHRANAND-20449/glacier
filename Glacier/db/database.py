from pymongo import MongoClient
from Glacier.config import MONGODB_URI

def get_database():
    client = MongoClient(MONGODB_URI)
    db = client.get_default_database()
    return db