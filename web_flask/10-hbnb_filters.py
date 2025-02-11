#!/usr/bin/python3
"""This module provides the `hbnb_filters` flask app"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    Display the Airbnb clone
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return (render_template("10-hbnb_filters.html",
                            states=states,
                            amenities=amenities))


@app.teardown_appcontext
def close_storage(self):
    """Hook that runs before app would be closed"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
