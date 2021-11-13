#!/usr/bin/python3
'''Unitest for base_model'''

import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ Test class for base model """

    def test_intantiation(self):
        """ New instance is created """
        a = FileStorage()
        self.assertTrue(type(a), FileStorage)
        self.assertTrue(isinstance(a, FileStorage))
        
if (__file__ == "__main__"):
    unittest.main()