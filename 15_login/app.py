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
	#print(request.cookies.get("username"))    
	return render_template('index.html')


@app.route("/auth")
def response():
	if request.args['username'] == user and request.args['password'] == pswd:
		return render_template("response.html",
                            	username = request.args['username'])
	else:
		return redirect("static/error.html")

@app.route("/out")
def logout():
	return redirect("/")
		

if __name__ == "__main__":
    app.debug = True
    app.run()
