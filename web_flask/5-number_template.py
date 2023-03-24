#!/usr/bin/python3
"""Flask web aplication with two routes"""
from flask import Flask
from flask import render_template

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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display3(text='is cool'):
    """Route "/" display
        Python text or Python is cool"""
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def display_num(n):
    """Route "/number/<n>" display n is a number"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_template(n):
    """Route "/number_template/<int:n>" display template"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    