#!/usr/bin/python3
"""
This module defines the entrypoint for a
simple Flask application.
"""

from flask import Flask, abort, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Returns a simple greeting message.

    Returns:
        str: A string containing message.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns a simple message.

    Returns:
        str: A string message.
    """
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Returns a simple message.

    Args:
        text (str): The text to be displayed in the message.

    Returns:
        str: A string containing the
        message with the specified text.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """
    Returns a simple message.

    Args:
        text (str): The text to be displayed in the message.

    Returns:
        str: A string containing the
        message with the specified text.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Returns a string message indicating
    whether a given number is an integer or not.

    Args:
        n (int): An integer.

    Returns:
        str: A string message indicating whether n is an integer or not.

    Raises:
        404: If n is not an integer.

    """
    if isinstance(n, int):
        return "{} is a number".format(n)
    else:
        return abort(404)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Returns an HTML page if n is an integer.

    Args:
        n (int): An integer.

    Returns:
        str: An HTML page if n is an integer.

    Raises:
        404: If n is not an integer.

    """
    if isinstance(n, int):
        return render_template('5-number.html', n=n)
    else:
        return abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
