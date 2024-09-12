#!/usr/bin/env python3

"""This modules starts a flask app"""

from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def index():
    """returns a simple json response"""

    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
