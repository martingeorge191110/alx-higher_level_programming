#!/usr/bin/python3
"""Test Rectangle class module"""
import unittest
from models import rectangle


class RectangleTest(unittest.TestCase):

    def testWithHieghtType(self):
        """tests width height x y not int"""
        with self.assertRaises(TypeError):
            result = rectangle.Rectangle(1.5, 15)
        with self.assertRaises(TypeError):
            result2 = rectangle.Rectangle(15, 1.5)
        with self.assertRaises(TypeError):
            result3 = rectangle.Rectangle(15, 15, 1.3, 2)
        with self.assertRaises(TypeError):
            result4 = rectangle.Rectangle(15, 15, 1, 2.1)

    def testWidthHightValue(self):
        """tests width height weather <= 0"""
        with self.assertRaises(ValueError):
            result = rectangle.Rectangle(-5, 10)
        with self.assertRaises(ValueError):
            result2 = rectangle.Rectangle(0, 10)
        with self.assertRaises(ValueError):
            result3 = rectangle.Rectangle(5, -10)
        with self.assertRaises(ValueError):
            result4 = rectangle.Rectangle(5, 0)

    def testXYValue(self):
        """tests x y < 0"""
        with self.assertRaises(ValueError):
            result = rectangle.Rectangle(5, 10, -5, 2)
        with self.assertRaises(ValueError):
            result2 = rectangle.Rectangle(5, 10, 2, -4)

if __name__ == "__main__":
    unittest.main()
