#!/usr/bin/python3
"""dhsn"""
from flask import Flask, render_template, abort, Response
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """close session sql"""
    storage.close()


@app.route("/states", strict_slashes=False)
def show_states():
    """show states"""
    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.route("/hbnb_filters", strict_slashes=False)
def filter_for_task():
    """show filters"""
    states = storage.all(State).values()
    amenity = storage.all(Amenity).values
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenity)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
