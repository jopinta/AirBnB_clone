#!/usr/bin/python3
'''Unitest for base_model'''

import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ Test class for base model """

    def test_filestorage(self):
        """testin"""
        a = BaseModel()
        b = FileStorage()
        c = {}


        self.assertNotEqual(c, models.storage.all())
        self.assertEqual(str, type(b._FileStorage__file_path)))

if (__file__ == "__main__"):
    unittest.main()
