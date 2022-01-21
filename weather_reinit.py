import time
import weather_integration
def weather_reinit(db_name,collection_name):
    
    client=weather_integration.Mongo_get_client()
    client.drop_database(db_name)
    client,db,collection=weather_integration.Mongo_init(db_name,collection_name)
    while True:
        weather_integration.Mongo_integration(collection)
        time.sleep(900)





