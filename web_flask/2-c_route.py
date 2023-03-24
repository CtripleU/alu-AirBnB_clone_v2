#!/usr/bin/python3
"""Flask web aplication with two routes"""
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


@app.route('/c/<text>', strict_slashes=False)
def display2(text):
    """Route "/c/<text>" display C text"""
    text1 = text.replace("_", " ")
    return 'C {}'.format(text1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
