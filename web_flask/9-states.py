#!/usr/bin/python3
"""This module provides the `states` flask app"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False, defaults={'id': 'None'})
@app.route("/states/<id>", strict_slashes=False)
def states(id):
    """
    Display a html page with the states of database or
    the cities according the passed state in the url
    """
    states = storage.all(State).values()
    return (render_template("9-states.html", id=id, states=states))


@app.teardown_appcontext
def close_storage(self):
    """Hook that runs before app would be closed"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
