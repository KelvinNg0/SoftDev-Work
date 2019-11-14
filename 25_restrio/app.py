# Kelvin Ng
# SoftDev pd2
# K25 -- Getting more REST
# 2019-11-13

from flask import Flask, render_template
import urllib.request as urllib2
import json

app = Flask(__name__)


@app.route("/")
def create():
    url = "https://www.metaweather.com/api/location/2459115/"
    u = urllib2.urlopen(url)
    response = u.read()
    data = json.loads(response)
    weather = data["consolidated_weather"][0]

    url = "http://ghibliapi.herokuapp.com/films?title=My%20Neighbor%20Totoro"
    u = urllib2.urlopen(url)
    response = u.read()
    data = json.loads(response)

    url = "http://rickandmortyapi.com/api/character/1"
    u = urllib2.urlopen(url)
    response = u.read()
    data = json.loads(response)

    return render_template("index.html", humid = weather['weather_state_name'], temp = data['the_temp'], date = data['applicable_date'])


if __name__ == "__main__":
    app.debug = True
    app.run()
