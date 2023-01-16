#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from io import StringIO


class TestRectangleClass(unittest.TestCase):
    def setUp(self):
        self.rect = Rectangle(10, 2)
        self.rect_copy = self.rect

    def tearDown(self):
        self.rect = self.rect_copy

    def test_rectangle_obj(self):
        self.assertEqual(self.rect.width, 10)
        self.assertEqual(self.rect.height, 2)

    def test_width_setter_getter(self):
        self.assertEqual(self.rect.width, 10)
        self.rect.width = 5
        self.assertEqual(self.rect.width, 5)

    def test_height_setter_getter(self):
        self.assertEqual(self.rect.height, 2)
        self.rect.height = 5
        self.assertEqual(self.rect.height, 5)

    def test_x_setter_getter(self):
        self.assertEqual(self.rect.x, 0)
        self.rect.x = 5
        self.assertEqual(self.rect.x, 5)

    def test_y_setter_getter(self):
        self.assertEqual(self.rect.y, 0)
        self.rect.y = 5
        self.assertEqual(self.rect.y, 5)

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
        with self.assertRaises(ValueError):
            self.rect.width = -1

        with self.assertRaises(ValueError):
            self.rect.height = -1

        with self.assertRaises(ValueError):
            self.rect.x = -1

        with self.assertRaises(ValueError):
            self.rect.y = -1

    def test_area(self):
        self.assertEqual(self.rect.area(), 20)

    def test_str(self):
        rec = Rectangle(4, 11)
        self.assertIsInstance(self.rect.__str__(), str)

    def test_update(self):
        update_list = [20, 60, 70, 15, 15]
        self.rect.update(*update_list)
        self.assertEqual(self.rect.id, 20)
        self.assertEqual(self.rect.width, 60)
        self.assertEqual(self.rect.height, 70)
        self.assertEqual(self.rect.x, 15)
        self.assertEqual(self.rect.y, 15)

        update_dict = {"id": 100, "width": 30, "height": 40, "x": 10, "y": 10}
        self.rect.update(**update_dict)
        self.assertEqual(self.rect.id, 100)
        self.assertEqual(self.rect.width, 30)
        self.assertEqual(self.rect.height, 40)
        self.assertEqual(self.rect.x, 10)
        self.assertEqual(self.rect.y, 10)

        self.rect.update(*update_list, **update_dict)
        self.assertEqual(self.rect.id, 20)
        self.assertEqual(self.rect.width, 60)
        self.assertEqual(self.rect.height, 70)
        self.assertEqual(self.rect.x, 15)
        self.assertEqual(self.rect.y, 15)

    def test_to_dictionary(self):
        obj_dict = self.rect.to_dictionary()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict.get("width", 0), 10)
        self.assertEqual(obj_dict.get("height", 0), 2)
