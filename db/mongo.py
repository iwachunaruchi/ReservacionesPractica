from pymongo import MongoClient
import os 
from dotenv import load_dotenv

load_dotenv()


class MongoConnection:
    def __init__(self):
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db = self.client[os.getenv('DB_NAME')]
    
    def get_db(self):
        return self.db

mongo_connection = MongoConnection()
