import time
import weather_integration
def weather_first(db_name,collection_name):
    ##Mongo db crée automatiquement la base de données ainsi que la collection lorsque elles n'existent pas encore
    client,db,collection=weather_integration.Mongo_init(db_name,collection_name)
    while True:
        weather_integration.Mongo_integration(collection)
        time.sleep(900)
