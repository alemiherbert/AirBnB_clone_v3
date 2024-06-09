#!/usr/bin/python3

"""
This module contains the routes for the index of the API.
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status():
    """
    Returns the status of the API.

    Returns:
        A dictionary containing the status of the API.
    """
    return {"status": "OK"}


@app_views.route("/stats", methods=["GET"], strict_slashes=False)
def stats():
    """
    Returns the count of all objects in the database.

    Returns:
        A dictionary containing the count of all objects in the database.
    """
    count_stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(count_stats)
