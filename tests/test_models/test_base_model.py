#!/usr/bin/python3
""" Unitest for base_model """
import unittest
from models.base_model import BaseModel

m = BaseModel()


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

    def test_to_dict(self):
        """ Test """
        m.my_number = 21
        m.name = "Fede tilt"
        m_d = m.to_dict()
        key = ["id", "name", "my_number", "created_at",
               "updated_at", "__class__"]

        self.assertCountEqual(m_d.keys(), key)
        self.assertEqual(m_d["__class__"], "BaseModel")
        self.assertEqual(m_d["my_number"], 21)
        self.assertEqual(m_d["name"], "Fede tilt")

    def test_str(self):
        """ Test """
        string = f"[{type(m).__name__}] ({m.id}) {m.__dict__}"
        self.assertEqual(string, str(m))


if __name__ == "__main__":
    unittest.main()
