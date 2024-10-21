#!/usr/bin/python3
"""test module Base class"""

import unittest
from models.base import Base

class BaseTest(unittest.TestCase):
    """Test BaseClass"""

    def setUp(self):
        # Accessing the private attribute directly to reset it
        Base._Base__nb_objects = 0

    def test_input_id(self):
        result = Base(12)
        self.assertEqual(result.id, 12)

    def test_nb_objects_id(self):
        res1 = Base()
        res2 = Base()
        res3 = Base()
        self.assertEqual(res1.id, 1)
        self.assertEqual(res2.id, 2)
        self.assertEqual(res3.id, 3)

    def test_combined_id(self):
        res1 = Base()
        res2 = Base(30)
        res3 = Base()
        self.assertEqual(res1.id, 1)
        self.assertEqual(res2.id, 30)
        self.assertEqual(res3.id, 2)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            result = Base(1, 2)

if __name__ == "__main__":
    unittest.main()
