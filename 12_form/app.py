# CleanCoal Kelvin Ng & David Xiedeng
# SoftDev1 pd1
# K12 
# 2019-10-02

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

user = 'cleancoal'
pswd = 'co2'

@app.route("/")
def renderTemp():
    return render_template('index.html')

@app.route("/auth")
def response():
	if request.args['username'] == user and request.args['password'] == pswd:
		return render_template("response.html",
                            	username = request.args['username'],
								password = request.args['password'],
                            	method = request.method)
	else:
		return redirect("static/error.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
