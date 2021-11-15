#!/usr/bin/python3
""" Unittest """
import unittest
import models
from models.base_model import BaseModel
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """ Test for State"""

    def test_state(self):
        """  Test for State """
        state = State()
        self.assertEqual(str, type(state.name))

if __name__ == '__main__':
    unittest.main()