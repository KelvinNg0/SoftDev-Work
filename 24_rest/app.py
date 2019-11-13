# Kelvin Ng
# SoftDev1 Pd1
# K24 : A RESTful Journey Skywards
# 2019-09-26

from flask import Flask, render_template
from json import loads
from urllib.request import urlopen

app = Flask(__name__)


@app.route("/")
def api():
    url = urlopen("https://api.nasa.gov/planetary/apod?api_key=f5dsiWP2TZ5cscN3jJviBarHppZKkdKqL5wZIcy2")
    response = url.read()
    data = loads(response)
    return render_template("api.html", pic = data['url'], description = data['explanation'])

if __name__ == "__main__":
	app.debug = True
	app.run()
