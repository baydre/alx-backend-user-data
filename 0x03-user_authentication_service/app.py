#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def create_app():
    """
    creates flask app that has
    a single route and return a
    JSON payload of the form.
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
