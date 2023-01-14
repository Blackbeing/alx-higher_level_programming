#!/usr/bin/python3
import unittest

from models.base import Base


class TestBaseClass(unittest.TestCase):

    def test_base_with_id(self):
        b = Base(19)
        self.assertEqual(b.id, 19)

    def test_base_without_id(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_base_with_negative_number(self):
        b = Base(-1)
        self.assertEqual(b.id, -1)


if __name__ == "__main__":
    unittest.main()
