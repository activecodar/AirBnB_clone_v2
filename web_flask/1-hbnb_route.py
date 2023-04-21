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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
