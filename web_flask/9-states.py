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


@app.route('/states/<id>', strict_slashes=False)
def cities_of_state(id):
    states = storage.all(State)
    state = None
    for state_nope in states.values():
        if state_nope.id == id:
            state = state_nope
            break
    if not state:
        error_message = "task 8 not working is giving me hives - chloe.c"
        abort(Response(error_message, 404))
    return render_template('9-states.html', state=state)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
