# RoastedDuck Kelvin Ng & Tanzim Elahi
# SoftDev1 pd1
# K12 -- Echo Echo Echo
# 2019-09-26  

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def renderTemp():
    return render_template('index.html')

@app.route("/auth")
def response():
    return render_template("response.html",
                            username = request.args['username'],
                            method = request.method)
 


if __name__ == "__main__":
    app.debug = True
    app.run()