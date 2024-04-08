#!/usr/bin/python3
"""define new route message"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hey_route():
    return "<p>Hello HBNB!</p>"


@app.route("/hbnb", strict_slashes=False)
def hey_route_2():
    return "<p>HBNB</p>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
