import collections
import time
import weather_integration
def weather_first(db_name,collection_name):
    client,db,collection=weather_integration.mongo_init(db_name,collection_name)
    return collection
db_name='weather_db'
collection_name='weather_collection'
collection=weather_first(db_name,collection_name)
while True:
    weather_integration.mongo_integration(collection)
    print('Time Stop')
    time.sleep(900)