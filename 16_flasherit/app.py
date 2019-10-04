# Team CleanCoal Kelvin Ng & David Xiedeng
# SoftDev1 pd1
# K#16 - Oh yes, perhaps I do…  
# 2019-10-03

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

user = 'cleancoal'
pswd = 'co2'
app.secret_key = 'YEET'

@app.route("/")
def renderTemp():
	if session.get('username') == user:
		return render_template("response.html",
                            	username = session['username'])
	return render_template('index.html')

@app.route("/auth")
def response():
	if request.args['username'] == user and request.args['password'] == pswd:
		session['username'] = request.args['username']
		return render_template("response.html",
                            	username = request.args['username'])
	if request.args['username'] != user and request.args['password'] == pswd:
		return redirect("/wrongUser")
	if request.args['username'] == user and request.args['password'] != pswd:
		return redirect("/wrongPswd")
	return redirect("/allWrong")

@app.route("/wrongUser")
def error0():
	return render_template('error.html', error = "Invalid Username")

@app.route("/wrongPswd")
def error1():
	return render_template('error.html', error = "Invalid Password")

@app.route("/allWrong")
def error2():
	return render_template('error.html', error = "Invalid Username and Password")

@app.route("/exit")
def logout():
	session.pop('username')
	return render_template('index.html')

if __name__ == "__main__":
	app.debug = True
	app.run()
