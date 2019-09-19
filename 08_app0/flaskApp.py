#Kelvin Ng
#SoftDev1 pd1
#K08 -- flaskApp0
#2019-09-18


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print(__name__)
    return "Hello World"

@app.route("/hello2")
def hello():
    print(__name__)
    return "Hello!"

@app.route("/HeLLo3")
def hi():
    print(__name__)
    return "Sup"

if __name__ == "__main__":
    app.debug = True
    app.run()