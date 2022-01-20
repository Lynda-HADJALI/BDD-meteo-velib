from flask import Flask, render_template
import json
app = Flask(__name__)
def loadVille():
    listOfVilles=[]
    with open('templates/ville.json',encoding='utf-8') as c:
         listOfVilles.append(json.load(c))
         return listOfVilles[0]

@app.route('/')
def home():
    return render_template("accueil.html")

@app.route('/', methods=['POST'])
def visualisation():
    return render_template("visualisation.html")





if __name__ == '__main__':
    app.run(debug = True)