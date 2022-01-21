import json

from flask import Flask, render_template, request, session, url_for, redirect





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
        return render_template('index.html')

    @app.route('/showSummary',methods=['POST'])
    def showSummary():
        com = [com for com in coms if com == request.form['com']]
        if com:
            com = [com for com in coms if com == request.form['com']][0]
            return render_template('welcome.html', com=com)
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