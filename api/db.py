# api/db.py
from pymongo import MongoClient

def get_db_collections(mongo_uri):
    client = MongoClient(mongo_uri)
    db = client['aula9']
    tasks_collection = db['livros']
    return tasks_collection, users_collection
