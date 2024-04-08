#!/usr/bin/python3
"""define new route for all State"""

from models import storage
from flask import Flask, render_template
from models.state import State
from models.city import City  # Import the City class

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Close the storage on teardown"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page with a list of all State objects in DBStorage."""
    states = storage.all(State).values()
    cities = storage.all(City).values()

    return render_template("8-cities_by_states.html",
                           cities=cities,
                           states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
