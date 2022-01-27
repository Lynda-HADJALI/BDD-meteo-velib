import time
import weather_integration
def drop_db(client,db_name):
    client.drop_database(db_name)
def weather_reinit(db_name,collection_name):   
    client=weather_integration.Mongo_get_client()
    drop_db(client,db_name)
    client,db,collection=weather_integration.Mongo_init(db_name,collection_name)
    return collection
db_name='weather_db'
collection_name='weather_collection'
collection=weather_reinit(db_name,collection_name)
while True:    
    weather_integration.Mongo_integration(collection)
    print('Time Stop')
    time.sleep(900)



