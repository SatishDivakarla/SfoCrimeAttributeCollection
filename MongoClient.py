__author__ = 'SatishDivakarla'
from pymongo import MongoClient

def mongodb_connections(database, collection):
    client = MongoClient('localhost', 27017)
    mongo_db = client[database];
    mongo_collection = mongo_db[collection];
    return mongo_collection


def isRecordsExists(collection, latitude, longitude):
    if(collection.find({"latitude" : str(latitude), 'longitude' : str(longitude)}).count() >0):
        return True
    else:
        return False
