import sqlite3

import requests

import time

import json

import datetime

def api_call():
    api ='https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&rows=1435&q=&sort=nom_arrondissement_communes&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes'
    json_data=requests.get(api).json()
    return json_data
def connection():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    return connection,cursor

def create_table(cur):
    create_table = "CREATE TABLE IF NOT EXISTS velib2 ( identifiant text, request_date numeric, commune text, station2 text, station_en_fonctionnement text, ebike INTEGER, ebikeavail INTEGER, capacity INTEGER, mechanical INTEGER)"

    cur.execute(create_table)    
def insert_data(connection,cur,json_data):
    DATEFORMAT = "%Y-%m-%d_%H-%M-%S"
    now = datetime.datetime.now()
    request_date = now.strftime(DATEFORMAT)

    for station in json_data["records"]:

        identifiant =station["fields"]["stationcode"]

        commune=station["fields"]["nom_arrondissement_communes"]

        station2=station["fields"]["name"]

        station_en_fonctionnement=station["fields"]["is_installed"]

        ebike=int(station["fields"]["ebike"])

        ebikeavail=int(station["fields"]["numbikesavailable"])

        capacity=int(station["fields"]["capacity"])

        mechanical = int(station["fields"]["mechanical"])

        cur.execute("""

        INSERT INTO velib2(identifiant, request_date,commune,station2,station_en_fonctionnement,ebike,ebikeavail,capacity,mechanical)

        VALUES(?, ?, ?, ?, ?, ?, ?, ?,?)""", (identifiant, request_date,commune,station2,station_en_fonctionnement,ebike,ebikeavail,capacity,mechanical))
        connection.commit()
def sql_integration(connection,cur):
    json_data=api_call()
    insert_data(connection,cur,json_data)
    print('Integration SQL Completed')













