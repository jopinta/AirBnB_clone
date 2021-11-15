#!/usr/bin/python3
'''Unitest for base_model'''
import unittest
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """Test Cases"""
    def test_Base(self):
        '''Test'''
        aee = BaseModel()
        a.name = "Fede"
        self.assertEqual(a.name, "Fede")


if __name__ == "__main__":
    unittest.main()
