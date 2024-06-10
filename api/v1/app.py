#!/usr/bin/python3

"""
This module is the main Flask application for the AirBnB clone API.
It initializes the Flask app, registers the blueprint for the API views,
and defines a teardown function to close the database connection.
"""

from flask import Flask, jsonify
from os import getenv
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_context(error):
    """
    Teardown function to close the database connection after each request.
    """
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """ handles 404 errors """
    status = {"error": "Not found"}
    return jsonify(status), 404


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST") or "0.0.0.0"
    port = getenv("HBNB_API_PORT") or 5000
    app.run(host=host, port=port, threaded=True, debug=True)
