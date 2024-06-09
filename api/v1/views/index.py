#!/usr/bin/python3

"""
This module contains the routes for the index of the API.
"""

from api.v1.views import app_views


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
    from models import storage
    from models.base_model import BaseModel
    from models.user import User
    from models.place import Place
    from models.city import City
    from models.state import State
    from models.amenity import Amenity
    from models.review import Review

    classes = {
        "users": User,
        "places": Place,
        "cities": City,
        "states": State,
        "amenities": Amenity,
        "reviews": Review
    }

    return {key: storage.count(value) for key, value in classes.items()}
