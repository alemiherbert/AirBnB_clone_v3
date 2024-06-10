#!/usr/bin/python3

"""
This module contains the unit tests for the API endpoints
of the AirBnB clone application.
"""

from flask import testing
from api.v1.app import app
from api.v1.views import *
import unittest


class TestApp(unittest.TestCase):
    """Test `app.py`."""

    def test_app_instance(self):
        with app.test_client() as c:
            """Test whether the app instance is created"""
            self.assertIsInstance(c, testing.FlaskClient)


if __name__ == "__main__":
    unittest.main()
