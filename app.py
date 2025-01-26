# beginning of app
from flask import Flask, render_template 
app = Flask(__name__) # creating app instance
# first route, function & route names need to be unique
@app.route("/") #decorator defines routes in app, in this case home '/'
def home():
    return render_template("index.html")

@app.route("/album") #second route has query parameter called 
def album():
    return render_template("album.html")

if __name__=="__main__":
    app.run()

