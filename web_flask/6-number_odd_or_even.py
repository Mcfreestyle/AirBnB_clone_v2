#!/usr/bin/python3
"""This module provides `hello`, `hbnb`, `c`, `python`,
   `number`, `number_template`, `number_odd_or_even` functions"""
from flask import Flask, render_template

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
    """Show a message with a passed parameter in the url"""
    text = text.replace('_', ' ')
    return ("C " + text)


@app.route("/python/", strict_slashes=False, defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """Show a message with a passed parameter in the url"""
    text = text.replace('_', ' ')
    return ("Python " + text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Show a message with a passed parameter(number) in the url"""
    return ("{} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Display a HTML page with a passed number in the url"""
    return (render_template("5-number.html", n=n))


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Display a HTML page according a passed number in the url"""
    return (render_template("6-number_odd_or_even.html", n=n))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
