import time
import json
from flask import request
import pymongo
import pprint
import matplotlib.pyplot as plt
def get_data():    
    client=pymongo.MongoClient('mongodb://localhost:27017/')
    db=client['weather_db']
    col=db['weather_collection']    
    return col
def find(col):
    return col.find()
def sort_recent(col):
    return col.find.sort("request_date",pymongo.DESCENDING)
def find_with_query(col,query):
    return col.find(query)
def count_documents(col):
    return col.count_documents({})
def count_documents_query(col,query):
    return col.count_documents(query)
def create_index(col):    
     index=col.create_index([('name',1)])
def plot_temp(col,town):
    weather=find_with_query({'name':town})
    temp=[]
    request_date=[]
    for w in weather:
        ##get temp for each period found in the db
        temp.append(w['main']['temp'])
        request_date.append(w['request_date'])
    return temp,request_date  
def plot(array1,array2,xlabel,ylabel):
    plt.plot(array1,array2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig('graphe.png')
      

    
    
    
    
    
    
    
    
    
