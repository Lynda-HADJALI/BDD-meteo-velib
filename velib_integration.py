import sqlite3

import requests

import time

import json

import datetime

def api_call():
    api ='https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&rows=1435&q=&sort=nom_arrondissement_communes&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes'
    velib_data=requests.get(api).json()
    return velib_data
def connection():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    return connection,cursor

def create_table(cur):
    create_table = "CREATE TABLE IF NOT EXISTS velib ( identifiant text, request_date numeric, commune text, station text, station_en_fonctionnement text, ebike INTEGER, ebikeavail INTEGER, capacity INTEGER, mechanical INTEGER)"

    cur.execute(create_table)    
def insert_data(connection,cur,velib_data):
    DATEFORMAT = "%Y-%m-%d_%H-%M-%S"
    now = datetime.datetime.now()
    request_date = now.strftime(DATEFORMAT)

    for station_ in velib_data["records"]:

        identifiant =station_["fields"]["stationcode"]

        commune=station_["fields"]["nom_arrondissement_communes"]

        station=station_["fields"]["name"]

        station_en_fonctionnement=station_["fields"]["is_installed"]

        ebike=int(station_["fields"]["ebike"])

        ebikeavail=int(station_["fields"]["numbikesavailable"])

        capacity=int(station_["fields"]["capacity"])

        mechanical = int(station_["fields"]["mechanical"])

        cur.execute("""

        INSERT INTO velib(identifiant, request_date,commune,station,station_en_fonctionnement,ebike,ebikeavail,capacity,mechanical)

        VALUES(?, ?, ?, ?, ?, ?, ?, ?,?)""", (identifiant, request_date,commune,station,station_en_fonctionnement,ebike,ebikeavail,capacity,mechanical))
        connection.commit()
def sql_integration(connection,cur):
    velib_data=api_call()
    insert_data(connection,cur,velib_data)
    print('Integration SQL Completed')













