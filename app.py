from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route("/breeds")
def breeds():
    URL = "https://dogapi.dog/api/v2/breeds"
    req = requests.get (url = URL)
    data = req.json()
    return render_template("index.html", data = data)

@app.route("/facts")
def facts():
    URL = "https://dogapi.dog/api/v2/facts?"
    req = requests.get (url = URL)
    data = req.json()
    return render_template("facts.html". data = data)

@app.route("/breeds{id}")
def breedsid():
    URL = "https://dogapi.dog/api/v2/breeds/"
    req = requests.get (url = URL)
    data = req.json()
    return render_template("breedsid.html", data = data)

