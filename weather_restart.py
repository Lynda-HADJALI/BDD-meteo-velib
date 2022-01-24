import collections
import time
import weather_integration
def weather_restart(db_name,collection_name):
    client,db,collection=weather_integration.Mongo_init(db_name,collection_name)
    return collection
db_name='weather_db'
collection_name='weather_collection'
collection=weather_restart(db_name,collection_name)
while True:
        weather_integration.Mongo_integration(collection)
        time.sleep(900)