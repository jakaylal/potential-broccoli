# beginning of app
from flask import Flask, render_template  # type: ignore
import requests # type: ignore
app = Flask(__name__) # creating app instance
# first route, function & route names need to be unique
@app.route("/") #decorator defines routes in app, in this case home '/'
def home():
    URL = "https://xkcd.com/info.0.json"
    req = requests.get(url = URL)
    data = req.json()
    return render_template("index.html", data = data)

@app.route("/pastComic") #decorator defines routes in app, in this case home '/'
def pastComic():
    URL = "https://xkcd.com/info.0.json"
    req = requests.get(url = URL)
    data = req.json()
    return render_template("index.html", data = data)

@app.route("/album") #second route has query parameter called 
def album():
    return render_template("album.html")

if __name__=="__main__":
    app.run()

