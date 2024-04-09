from flask import Flask, render_template, abort
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def display_states():
    """Displays states"""
    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def cities_of_state(id):
    few_states = storage.all(State)
    state = None
    for utah in few_states.values():
        if utah.id == id:
            state = utah
            break
    if state is None:
        return render_template('9-states.html', message="Not found!")
    cities = state.cities
    return render_template('9-states.html', state=state, cities=cities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
