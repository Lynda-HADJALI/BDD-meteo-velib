import requests
import time
import json
import pymongo
def list_cities():
    api ="https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&rows=1435&q=&sort=nom_arrondissement_communes&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes"
    json_data = requests.get(api).json()
    communes_list=json_data['facet_groups'][4]['facets']
    communes=[]

    for i in range(0,len(communes_list)):
        communes.append(communes_list[i]['name'])
    communes.sort()
    return communes
def data_change(json_file):
    json_file['sys']['sunrise']= time.strftime('%I:%M:%S', time.gmtime(json_file['sys']['sunrise']+json_file['timezone']))
    json_file['sys']['sunset']= time.strftime('%I:%M:%S', time.gmtime(json_file['sys']['sunset']+json_file['timezone']))
    json_file['dt']= time.strftime('%I:%M:%S', time.gmtime(json_file['dt']+json_file['timezone']))
    json_file.pop('timezone')
    return json_file
def api_call(city,units):
    api='https://api.openweathermap.org/data/2.5/weather?q='+city +'&appid=a71c550b866a5dad0736bc6f5e7508da&units='+units
    json_data = requests.get(api)
    print(json_data.status_code)
    json_data=json_data.json()
    return json_data
def Mongo_get_client():
    client=pymongo.MongoClient('mongodb://localhost:27017/')
    return client
def Mongo_get_db(client,db_name):
    db=client[db_name]
    return db
def Mongo_get_collection(db,collection_name):
    collection=db[collection_name]
    return collection

def Mongo_init(db_name,collection_name):
    client=Mongo_get_client
    db=Mongo_get_db(client,db_name)
    collection=Mongo_get_collection(db,collection_name)
    return client,db,collection
    
def Mongo_integration(collection):
    units='metric'
    for city in list_cities():
        json_data=api_call(city,units)
        json_data=data_change(json_data)
        x=collection.insert_one(json_data)
client,db,collection=Mongo_init('weather_db','weather_collection')
while True:   
    Mongo_integration(collection)
    time.sleep(900)
