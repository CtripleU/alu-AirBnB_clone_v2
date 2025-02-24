#!/usr/bin/python3
"""Flask web aplication  listening on 0.0.0.0, port 5000"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display():
    """Route "/" display Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display1():
    """Route "/hbnb" display HBNB"""
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
