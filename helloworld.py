from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello():

    message = "<h1 style=\"color: #001cff;\">Hello World from Intel Cloud.U</h1>"

    return (message)


app.run(host='0.0.0.0', port=8080, debug=True)
