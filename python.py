import sqlite3

import requests

import time

import json



api ='https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&rows=1435&q=&sort=nom_arrondissement_communes&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes'

json_data = requests.get(api).json()







connection = sqlite3.connect('data.db')



cursor = connection.cursor()



create_table = "CREATE TABLE IF NOT EXISTS velib2 ( identifiant text, request_date int, commune text, station2 text, station_en_fonctionnement text, ebike INTEGER, ebikeavail INTEGER, capacity INTEGER, mechanical INTEGER)"

cursor.execute(create_table)



startime = time.time()

request_date = int(time.time())

for station in json_data["records"]:

    identifiant =station["fields"]["stationcode"]

    commune=station["fields"]["nom_arrondissement_communes"]

    station2=station["fields"]["name"]

    station_en_fonctionnement=station["fields"]["is_installed"]

    ebike=int(station["fields"]["ebike"])

    ebikeavail=int(station["fields"]["numbikesavailable"])

    capacity=int(station["fields"]["capacity"])

    mechanical = int(station["fields"]["mechanical"])

    cursor.execute("""

    INSERT INTO velib2(identifiant, request_date,commune,station2,station_en_fonctionnement,ebike,ebikeavail,capacity,mechanical)

     VALUES(?, ?, ?, ?, ?, ?, ?, ?,?)""", (identifiant, request_date,commune,station2,station_en_fonctionnement,ebike,ebikeavail,capacity,mechanical))



    connection.commit()



endtime = time.time()
