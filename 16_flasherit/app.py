# Team CleanCoal Kelvin Ng & David Xiedeng
# SoftDev1 pd1
# K#16 - Oh yes, perhaps I do…  
# 2019-10-03

from flask import Flask, render_template, request, redirect, session, flash
import os

app = Flask(__name__)

user = 'cleancoal'
pswd = 'co2'
app.secret_key = os.urandom(32)

@app.route("/")
def renderTemp():
	if "username" in session:
		flash("You are already logged in!")
		return render_template("response.html",
                            	username = session['username'])
	return render_template('index.html')

@app.route("/auth")
def response():
	if request.args['username'] == user and request.args['password'] == pswd:
		session['username'] = request.args['username']
		flash("Hello " + session['username'] + "! You have successfully logged in.")
		return render_template("response.html")
	if request.args['username'] != user and request.args['password'] == pswd:
		return redirect("/wrongUser")
	if request.args['username'] == user and request.args['password'] != pswd:
		return redirect("/wrongPswd")
	return redirect("/allWrong")

@app.route("/wrongUser")
def error0():
	flash("Invalid Username")
	return render_template('error.html')

@app.route("/wrongPswd")
def error1():
	flash("Invalid Password")
	return render_template('error.html')

@app.route("/allWrong")
def error2():
	flash("Invalid Username and Password")
	return render_template('error.html')

@app.route("/exit")
def logout():
	session.pop('username')
	return render_template('index.html')

@app.route("/retry")
def retry():
	return render_template('index.html')

if __name__ == "__main__":
	app.debug = True
	app.run()
