#!/usr/bin/python3

"""This module contains the implementation of the State API endpoints.

It provides the following routes:
- GET /api/v1/states: Retrieves a list of all states
- GET /api/v1/states/<state_id>: Retrieves a specific state
- POST /api/v1/states: Creates a new state
- PUT /api/v1/states/<state_id>: Updates a specific state
- DELETE /api/v1/states/<state_id>: Deletes a specific state
"""

from flask import jsonify, abort, request
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route("/states", methods=["GET"])
def states():
    """retrieve a list of all state objects"""
    states = storage.all("State").values()
    all_states = []
    for state in states:
        all_states.append(state.to_dict())
    return jsonify(all_states)


@app_views.route("states/<state_id>", methods=["GET"])
def state_get(state_id):
    """retrieve a specific state object"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route("/states/<state_id>", methods=["DELETE"])
def state_delete(state_id):
    """delete a specified state object"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    state.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route("/states", methods=["POST"])
def state_post(state_id):
    """create a new state object"""
    if not request.json:
        abort(400, "Not a JSON")
    if "name" not in request.json:
        abort(400, "Missing name")
    new_state = State(**request.json)
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route("/states/<state_id>", methods=["PUT"])
def state_put(state_id):
    """update a specified state object"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    if not request.json:
        abort(400, "Not a JSON")
    for key, value in request.json.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200
