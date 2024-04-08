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


@app.route("/number_template/<int:n>")
def html_is_back(n):
    try:
        n = int(n)
        return render_template('5-number.html', n=n)
    except ValueError:
        return (
            "Ooh, black and yellow!\n"
            "Let's shake it up a little.\n"
            "Barry! Breakfast is ready!\n"
            "Coming!\n"
            "Hang on a second.\n"
            "Hello?\n"
            "Barry?\n"
            "Adam?\n"
            "Can you believe this is happening?\n"
            "I can't.\n"
            "I'll pick you up.\n"
            "Looking sharp.\n"
            "Use the stairs, Your father paid good money for those."
        )


@app.route("/number_odd_or_even/<int:n>")
def html_task_6(n):
    try:
        n = int(n)
        return render_template('6-number_odd_or_even.html', n=n)
    except ValueError:
        return (
            "Sorry. I'm excited.\n"
            "Here's the graduate.\n"
            "We're very proud of you, son.\n"
            "A perfect report card, all B's.\n"
            "Very proud.\n"
            "Ma! I got a thing going here.\n"
            "You got lint on your fuzz.\n"
            "Ow! That's me!\n"
            "Wave to us! We'll be in row 118,000.\n"
            "Bye!\n"
            "Barry, I told you, stop flying in the house!\n"
            "Hey, Adam.\n"
            "Hey, Barry.\n"
            "Is that fuzz gel?\n"
            "A little. Special day, graduation."
        )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
