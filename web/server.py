import json
import sqlite3
from flask import Flask, render_template, request, session, url_for, redirect
import weather_data
import sql_data
import pymongo
def loadCom():
    with open('ville.json') as com:
         listOfCom = json.load(com)
         return listOfCom

def create_app(config): 
    app = Flask(__name__)
    app.secret_key = 'something_special'
    app.config.from_object("config")
    app.config["TESTING"] = config.get("TESTING")


    coms = loadCom()
    
    @app.route('/')
    def index():
        return render_template('index.html',coms=coms)

    @app.route('/showStation',methods=['POST'])
    def showStation():
         com = [com for com in coms if com == request.form['com']]
         weather_collection=weather_data.get_data()
         if com:
             com = [com for com in coms if com == request.form['com']][0]
             cur=sql_data.sql_connection()
             elem_name='station2,ebike,mechanical'
             order_name='request_date'
             query='commune=:town and station_en_fonctionnement=:boolean'
             dico={'town':com,'boolean':'OUI'}
             res=sql_data.select_with_order(cur,elem_name,order_name,query,dico)
             list_station=[]
             for q in res:
                 list_station.append(q)
             is_returning=list_station[0]    
             query={'name':com}
             sorted_elem="request_date"
             param=pymongo.DESCENDING
             r=weather_data.get_recent(weather_collection,query,sorted_elem,param)
             list_weather=[]
             for w in r:
                list_weather.append(w)
             w_info=list_weather[0]
        
             return render_template('welcome.html',w_info=w_info,is_returning=is_returning)
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