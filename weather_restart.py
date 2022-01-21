import time
import weather_integration
def weather_first(db_name,collection_name):
    client,db,collection=weather_integration.Mongo_init(db_name,collection_name)
    while True:
        weather_integration.Mongo_integration(collection)
        time.sleep(900)
