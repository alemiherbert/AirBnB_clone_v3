#!/usr/bin/python3

"""
This module contains the unit tests for the API endpoints
in the v1 version of the AirBnB clone.
"""

from api.v1.app import *
import unittest
import pep8
from os import getenv
import requests
import json


storage = getenv("HBNB_TYPE_STORAGE")


class TestIndex(unittest.TestCase):
    """Test the index file of the API."""

    def test_status(self):
        """Test the /status route of the API."""
        with app.test_client() as c:
            resp = c.get('/api/v1/status')
            data = json.loads(resp.data.decode('utf-8'))
            self.assertEqual(data, {'status': 'OK'})

    def test_stats(self):
        """Test the /stats route of the API."""
        with app.test_client() as c:
            resp = c.get('/api/v1/stats')
            data = json.loads(resp.data.decode('utf-8'))
            for k, v in data.items():
                self.assertIsInstance(v, int)
                self.assertTrue(v >= 0)


if __name__ == '__main__':
    unittest.main()
