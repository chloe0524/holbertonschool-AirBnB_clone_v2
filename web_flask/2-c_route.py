#!/usr/bin/python3
"""define new route message with value attached to it"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hey_route():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hey_route_2():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text_route(text):
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
