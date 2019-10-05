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
                            	username = session['username']) # user is redirected to the response page if logged in
	return render_template('index.html') # returns default page if user is not logged in

@app.route("/auth")
def response():
	if request.args['username'] == user and request.args['password'] == pswd:
		session['username'] = request.args['username']	# starts a session if user inputs correct username and password
		flash("Hello " + session['username'] + "! You have successfully logged in.")	# flashes welcome message
		return render_template("response.html")		# user is then redirected to response page
	if request.args['username'] != user and request.args['password'] == pswd:
		return redirect("/wrongUser")	# if username is wrong and password is correct, user is redicreted to error page
	if request.args['username'] == user and request.args['password'] != pswd:
		return redirect("/wrongPswd")	# if username is correct and password is wrong, user is redicreted to error page
	return redirect("/allWrong")	# if both username and password is wrong, user is redicreted to error page

@app.route("/wrongUser")
def error0():
	flash("Invalid Username")	# flashes error message
	return render_template('error.html')	# redirects to error page

@app.route("/wrongPswd")
def error1():
	flash("Invalid Password")	# flashes error message
	return render_template('error.html')	# redirects to error page

@app.route("/allWrong")
def error2():
	flash("Invalid Username and Password")		# flashes error message
	return render_template('error.html')	# redirects to error page

@app.route("/exit")
def logout():
	session.pop('username')		# when logging out, the session is removed
	return render_template('index.html')	# redircts to login page

@app.route("/retry")
def retry():
	return render_template('index.html')	# retry button in html that redircts to login page if either or both the password and username is wrong

if __name__ == "__main__":
	app.debug = True
	app.run()
