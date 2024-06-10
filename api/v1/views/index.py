#!/usr/bin/python3

"""
This module contains the routes for the index of the API.
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


classes = {"users": "User", "places": "Place", "states": "State",
           "cities": "City", "amenities": "Amenity",
           "reviews": "Review"}


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status():
    """
    Returns the status of the API.

    Returns:
        A dictionary containing the status of the API.
    """
    return jsonify({"status": "OK"})


@app_views.route("/stats", methods=["GET"], strict_slashes=False)
def stats():
    """
    Returns the count of all objects in the database.

    Returns:
        A dictionary containing the count of all objects in the database.
    """
    count_dict = {}
    for cls in classes:
        count_dict[cls] = storage.count(classes[cls])
    return jsonify(count_dict)
