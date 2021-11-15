#!/usr/bin/python3
"""Unitest for Review"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test review"""

    def test_amenity(self):
        """Test"""
        review = Review()
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")


if __name__ == "__main__":
    unittest.main()