#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    def test_rectangle_obj(self):
        rect = Rectangle(10, 2)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 2)

    def test_width_setter_getter(self):
        rect = Rectangle(10, 2)
        self.assertEqual(rect.width, 10)
        rect.width = 5
        self.assertEqual(rect.width, 5)

    def test_height_setter_getter(self):
        rect = Rectangle(10, 2)
        self.assertEqual(rect.height, 2)
        rect.height = 5
        self.assertEqual(rect.height, 5)

    def test_x_setter_getter(self):
        rect = Rectangle(10, 2)
        self.assertEqual(rect.x, 0)
        rect.x = 5
        self.assertEqual(rect.x, 5)

    def test_y_setter_getter(self):
        rect = Rectangle(10, 2)
        self.assertEqual(rect.y, 0)
        rect.y = 5
        self.assertEqual(rect.y, 5)
