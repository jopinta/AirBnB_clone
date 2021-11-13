#!/usr/bin/python3
'''Unitest for Users'''
import unittest
from models.user import User


class TestBase(unittest.TestCase):
    '''Test Cases'''

    def test_User(self):
        '''Test'''
        a = User()
        a.email = "Fede"
        self.assertEqual(a.email, "Fede")


if __name__ == "__main__":
    unittest.main()
