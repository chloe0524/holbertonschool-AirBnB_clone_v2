#!/usr/bin/python3
"""define host + port + route message"""

from flask import Flask

app = Flask(__name__)
strict_slashes=False

@app.route("/")
def hey_route():
    return "<p>Hello HBNB!</p>", '/'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)