#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([2, 8, 5]), 8)
        self.assertEqual(max_integer([2, -8, 5]), 5)
        self.assertEqual(max_integer([]), None)


if __name__ == "__main__":
    unittest.main()
