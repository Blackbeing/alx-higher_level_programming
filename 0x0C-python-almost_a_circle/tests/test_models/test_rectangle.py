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

    def test_args_are_ints(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 2, 1, 1)

        with self.assertRaises(TypeError):
            Rectangle(10, "2", 1, 1)

        with self.assertRaises(TypeError):
            Rectangle(10, 2, "1", 1)

        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, "1")

    def test_args_values_ranges(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 10)

        with self.assertRaises(ValueError):
            Rectangle(10, 0)

        with self.assertRaises(ValueError):
            Rectangle(10, 10, -1)

        with self.assertRaises(ValueError):
            Rectangle(10, 10, 1, -1)

    def test_setters_validate_value(self):
        rect = Rectangle(10, 10)
        with self.assertRaises(ValueError):
            rect.width = -1

        with self.assertRaises(ValueError):
            rect.height = -1

        with self.assertRaises(ValueError):
            rect.x = -1

        with self.assertRaises(ValueError):
            rect.y = -1
