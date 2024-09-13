#!/usr/bin/env python3

"""This modules starts a flask app"""

from flask import Flask, abort, jsonify, request
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def index():
    """returns a simple json response"""

    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def register_user():
    """API to register a new user"""

    user_payload = request.form

    if user_payload is None:
        abort(400, description="Not a JSON")

    email = user_payload.get('email')
    password = user_payload.get('password')

    try:
        AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    return jsonify({"email": email, "message": "user created"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
