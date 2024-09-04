'''
This is a basic flask application.
'''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    '''Returns hello World!'''
    return "<p>Hello, World!</p>"
