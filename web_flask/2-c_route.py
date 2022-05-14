#!/usr/bin/python3
"""This module provides `hello`, `hbnb`, `c` functions"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Show a message"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Show a message"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Show a message with an passed parameter in the url"""
    text = text.replace('_', ' ')
    return ("C " + text)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
