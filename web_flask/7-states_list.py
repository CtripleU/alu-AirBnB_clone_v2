#!/usr/bin/python3
"""FlasK web aplication"""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_HTML():
    """Display html page with States"""
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def delete_SQLA(self):
    """Remove the current SQLAlchemySession"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
