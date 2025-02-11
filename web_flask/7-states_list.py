#!/usr/bin/python3
"""This module provides the `states_list` flask app"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Display a html page with the states list"""
    states = storage.all(State).values()
    return (render_template("7-states_list.html", states=states))


@app.teardown_appcontext
def close_storage(self):
    """Hook that runs before app would be closed"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
