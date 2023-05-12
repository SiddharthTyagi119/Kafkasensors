import pymongo
import os


import certifi
ca = certifi.where()

class MongodbOperation:

    def __init__(self) -> None:
        #client to connect with mongo db server, passing the url of client
        MONGO_DB_URL="mongodb+srv://sidtyagi05:Corona1212@cluster0.thnqzt7.mongodb.net/"
        self.client = pymongo.MongoClient(MONGO_DB_URL,tlsCAFile=ca)
        #creating db
        self.db_name="ineuron"

    #inserting the records
    #as soon as we are consuming the 5000 records, once you have 5000 records from kafka in consumer then only we dump the data in mongo db in one attempt 
    def insert_many(self,collection_name,records:list):
        self.client[self.db_name][collection_name].insert_many(records)

    def insert(self,collection_name,record):
        self.client[self.db_name][collection_name].insert_one(record)
        
