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
def Mongo_init():
    client=pymongo.MongoClient('mongodb://localhost:27017/')
    db=client['weather_db']
    coll=db['weather_collection']
    return coll
    
def Mongo_integration(coll):
    units='metric'
    for city in list_cities():
        json_data=api_call(city,units)
        json_data=data_change(json_data)
        x=coll.insert_one(json_data)
coll=Mongo_init()
while True:   
    Mongo_integration(coll)
    time.sleep(90)
