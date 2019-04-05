#!flask/bin/python
from flask import Flask

app = Flask(____name____)

@app.route('/')
def index():
    return "Hello World"

if ____name____ == '____main____':
    app.run(debug=True)