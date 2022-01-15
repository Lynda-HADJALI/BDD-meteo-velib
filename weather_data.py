import time
import json
import pymongo
import pprint
def get_data():
    client=pymongo.MongoClient('mongodb://localhost:27017/')
    db=client['weather_db']
    col=db['weather_collection']    
    return col
def find(col):
    return col.find()
def find_with_query(col,query):
    return col.find(query)
def count_documents(col):
    return col.count_documents({})
def count_documents_query(col,query):
    return col.count_documents(query)
def create_index(col,index):
     client=pymongo.MongoClient('mongodb://localhost:27017/')
     db=client['weather_db']
     col=db['weather_collection']
     index=col.create_index([('name')])
     return index
col=get_data()
pprint.pprint(count_documents(col))
query={'name':'Paris'}

r=find_with_query(col,query)
for town in r:
	pprint.pprint(town)


    
    
    
    
    
    
    
    
    
