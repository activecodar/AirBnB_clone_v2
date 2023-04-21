#!/usr/bin/python3
"""
This module defines the entrypoint for a
simple Flask application.
"""

from flask import Flask

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
