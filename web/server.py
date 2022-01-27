import json
import sqlite3
from flask import Flask, render_template, request, session, url_for, redirect
import weather_data
import sql_data
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
             elem_name='station2,ebike,mechanical,'
             query='commune>:com_name and station_en_fonctionnement=:boolean'
             dico={'com_name':com,'boolean':'OUI'}
             query_response=sql_data.find_elem_with_query(cur,query,elem_name,dico)
             ##result = cur.execute(req)
             weather_query=query={'name':com}  
             weather=weather_data.find_with_query(weather_collection,weather_query)
             for weather_info in weather:
                w_info=weather_info
             return render_template('welcome.html',w_info=w_info,is_returning=query_response)
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