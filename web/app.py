from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("accueil.html")

@app.route('/', methods=['POST'])
def visualisation():
    return render_template("visualisation.html")





if __name__ == '__main__':
    app.run(debug = True)