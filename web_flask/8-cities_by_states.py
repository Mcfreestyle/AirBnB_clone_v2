#!/usr/bin/python3
"""This module provides the `cities_by_states` flask app"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Display a html page with the cities list according the state"""
    states = storage.all(State).values()
    return (render_template("8-cities_by_states.html", states=states))


@app.teardown_appcontext
def close_storage(self):
    """Hook that runs before app would be closed"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
