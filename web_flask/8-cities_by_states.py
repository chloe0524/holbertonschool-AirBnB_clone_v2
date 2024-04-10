#!/usr/bin/python3
"""df"""

from models.state import State
from models import storage
from flask import render_template, Flask

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """djhfdj:"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    states = storage.all('State')
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
