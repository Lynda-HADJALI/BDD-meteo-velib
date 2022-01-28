import pymongo


def connect_to_mongo():    
    client= pymongo.MongoClient( 'mongodb://localhost:27017/')
    db= client['weather_db']
    col= db['weather_collection']    
    return col


def find(col):
    return col.find()


def sort_weather_data(col, query, sort_by_field, sort_order):
    return col.find(query).sort(sort_by_field, sort_order)


def find_with_query(col, query):
    return col.find(query)


def count_documents(col):
    return col.count_documents({})


def count_documents_query(col, query):
    return col.count_documents(query)


def create_index(col):    
    index=col.create_index([('name', 1)])
    return index
      

    
    
    
    
    
    
    
    
    
