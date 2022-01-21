import time
import weather_integration
##Mongo db crée automatiquement la base de données ainsi que la collection lorsque elles n'existent pas encore
client,db,collection=weather_integration.Mongo_init('weather_db','weather_integration')
while True:
    weather_integration.Mongo_integration(collection)
    time.sleep(900)
