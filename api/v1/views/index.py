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
