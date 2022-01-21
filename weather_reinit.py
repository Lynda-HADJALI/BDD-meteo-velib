import time
import weather_integration
client=weather_integration.Mongo_get_client()
client.drop_database('weather_db')
client,db,collection=weather_integration.Mongo_init('weather_db','weather_integration')
while True:
    weather_integration.Mongo_integration(collection)
    time.sleep(900)





