#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, jsonify, request, redirect, abort
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def create_app():
    """
    creates flask app that has
    a single route and return a
    JSON payload of the form.
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def register_user():
    """
    end-point to register a user
    the POST /users route.
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """
    implements login function to respond
    to POST /sessions route
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)

    response = jsonify({'email': email, 'message': 'logged in'})
    response.set_cookie("session_id", session_id)

    return response


@app.route('/sessions', methods=['DELETE'])
def logout():
    """
    implement logout function to respond
    to DELETE /sessions route.
    """
    session_id = request.cookies.get("session_id")

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)

    AUTH.destroy_session(user['user.id'])
    return redirect('/')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
