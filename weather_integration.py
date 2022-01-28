import requests
import time
import json
import pymongo
import datetime
def list_cities():
    api ="https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&rows=1435&q=&sort=nom_arrondissement_communes&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes"
    json_data = requests.get(api).json()
    communes_list=json_data['facet_groups'][4]['facets']
    communes=[]

    for i in range(0,len(communes_list)):
        communes.append(communes_list[i]['name'])
    communes.sort()
    return communes
def preprocess_data(json_weather_data):
    DATEFORMAT = "%Y-%m-%d_%H-%M-%S"
    now = datetime.datetime.now()
    request_date = now.strftime(DATEFORMAT)
    json_weather_data['sys']['sunrise']= time.strftime('%I:%M:%S', time.gmtime(json_weather_data['sys']['sunrise']+json_weather_data['timezone']))
    json_weather_data['sys']['sunset']= time.strftime('%I:%M:%S', time.gmtime(json_weather_data['sys']['sunset']+json_weather_data['timezone']))
    json_weather_data['dt']= time.strftime('%I:%M:%S', time.gmtime(json_weather_data['dt']+json_weather_data['timezone']))
    json_weather_data['request_date']=request_date
    json_weather_data.pop('timezone')
    return json_weather_data
def api_call(city,units):
    api='https://api.openweathermap.org/data/2.5/weather?q='+city +'&appid=a71c550b866a5dad0736bc6f5e7508da&units='+units
    weather_data = requests.get(api)
    weather_data_to_json=weather_data.json()
    return weather_data_to_json
def mongo_get_client():
    client=pymongo.MongoClient('mongodb://localhost:27017/')
    return client
def mongo_get_db(client,db_name):
    db=client[db_name]
    return db
def mongo_get_collection(db,collection_name):
    collection=db[collection_name]
    return collection

def mongo_init(db_name,collection_name):
    client=mongo_get_client()
    db=mongo_get_db(client,db_name)
    collection=mongo_get_collection(db,collection_name)
    return client,db,collection
    
def mongo_integration(collection):
    units='metric'
    for city in list_cities():
        request_weather_data=api_call(city,units)
        json_weather_data=preprocess_data(request_weather_data)
        x=collection.insert_one(json_weather_data)
    print('Integration Mongo Completed')