#!/usr/bin/python3
"""Test Base class module"""
import unittest
from models import base


class BaseTest(unittest.TestCase):
    """Test BaseClass"""

    def test_setId(self):
        result = base.Base(20)
        result2 = base.Base(None)
        self.assertEqual(result.id, 20)
        self.assertEqual(result2.id, 1)

if __name__ == "__main__":
    unittest.main()
