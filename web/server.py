import json
import sqlite3
from flask import Flask, render_template, request, session, url_for, redirect
import weather_data
import velib_data
import pymongo
def load_com():
    with open('ville.json') as com:
         list_Of_com = json.load(com)
         return list_Of_com

def create_app(config): 
    app = Flask(__name__)
    app.secret_key = 'something_special'
    app.config.from_object("config")
    app.config["TESTING"] = config.get("TESTING")


    coms = load_com()
    
    @app.route('/')
    def index():
        return render_template('index.html',coms=coms)

    @app.route('/showStation',methods=['POST'])
    def showStation():
         com = [com for com in coms if com == request.form['com']]
         weather_collection=weather_data.connect_to_mongo()
         if com:
             com = [com for com in coms if com == request.form['com']][0]
             connection = sqlite3.connect('../data.db')
             cur = connection.cursor()
             column_name='station,ebike,mechanical'
             order_by_column='request_date'
             query='commune=:town and station_en_fonctionnement=:boolean'
             query_arguments={'town':com,'boolean':'OUI'}
             res=velib_data.query_with_order(cur,column_name,order_by_column,query,query_arguments)
             list_station=[]
             for q in res:
                 list_station.append(q)
             most_recent_station=list_station[0]    
             query={'name':com}
             sort_by_field="request_date"
             sort_order=pymongo.DESCENDING
             r=weather_data.sort_weather_data(weather_collection,query,sort_by_field,sort_order)
             list_weather=[]
             for w in r:
                list_weather.append(w)
             most_recent_weather=list_weather[0]
        
             return render_template('welcome.html',most_recent_weather=most_recent_weather,most_recent_station=most_recent_station)
         else :
             
             error='Desole, cette communes ne contient pas de velib'
             return render_template('index.html', error=error)

    @app.route('/logout')
    def logout():
        return redirect(url_for('index'))
    
    return app

app = create_app({"TESTING": False})


if __name__ == "__main__":
    app.run(debug=True)