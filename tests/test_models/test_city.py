#!/usr/bin/python3
"""Unitest for City"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test Cases"""

    def test_City(self):
        """Test"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == "__main__":
    unittest.main()
