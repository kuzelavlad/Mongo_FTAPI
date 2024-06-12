import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
mongodb_uri = os.environ.get('MONGODB_URI')

client = MongoClient(mongodb_uri)
db = client.mongo_db

collection_name = db['users_collection']