from flask import Flask
from flask import render_template
from datetime import datetime
import re
import json
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('C:/nodeSystem/dist/index.html')

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content

@app.route("/widgets/get")
def getData(): 
    return json.dumps([
        {
            'foo': 1,
            'hello': 'hi'
        },
        {
            'foo': 2,
            'hello': 'howdy'
        },
        {
            'foo': 3,
            'hello': 'hola'
        },
        {
            'foo': 4,
            'hello': 'ahoy'
        }
    ])