#!/usr/bin/python3
"""define new route message if n is integer"""

from flask import Flask, render_template


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


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def snake_text(text):
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def num_number_route(n):
    try:
        n = int(n)
        return "{} is a number".format(n)
    except ValueError:
        return (
            "{}, According to all known laws of aviation, there is no way "
            "a bee should be able to fly. Its wings are too small to get "
            "its fat little body off the ground. The bee, of course, flies "
            "anyway because bees don't care what humans think is impossible. "
            "Yellow, black. Yellow, black. Yellow, black. Yellow, black."
            .format(n)
        )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
