#!/usr/bin/python3
""" Unitest for base_model """
import unittest
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """ Test Cases """
    def test_Base(self):
        """ Test """
        a = BaseModel()
        a.name = "Fede"
        self.assertEqual(a.name, "Fede")

    def test_save(self):
        """ Test """
        m = BaseModel()
        created_at_a = m.created_at
        updated_at_a = m.updated_at
        m.save()
        created_at_b = m.created_at
        updated_at_b = m.updated_at
        self.assertEqual(created_at_a, created_at_b)
        self.assertNotEqual(updated_at_a, updated_at_b)


if __name__ == "__main__":
    unittest.main()
