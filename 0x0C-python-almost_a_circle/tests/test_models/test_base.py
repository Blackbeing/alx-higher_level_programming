#!/usr/bin/python3
import unittest

from models.base import Base
from models.rectangle import Rectangle
from pathlib import Path


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

    def test_base_to_json_string(self):
        b = Base(2)
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        assert isinstance(b.to_json_string(list_input), str)

        list_input2 = []
        self.assertEqual(b.to_json_string(list_input2), "[]")

    def test_save_to_file(self):
        d = {'id': 89, 'width': 10, 'height': 4}
        obj = Rectangle.create(**d)
        obj.save_to_file([obj])

        assert obj.__class__.__name__ == "Rectangle"
        assert Path("Rectangle.json").exists()

        obj.save_to_file([])
        with open("Rectangle.json", 'r') as fd:
            self.assertEqual(fd.read(), "[]")

    def test_from_json_string(self):
        b = Base(3)
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_str = b.to_json_string(list_input)
        assert isinstance(b.from_json_string(json_str), list)

    def test_create(self):
        d = {'id': 89, 'width': 10, 'height': 4}
        obj = Rectangle.create(**d)

        assert type(obj) is Rectangle
        self.assertEqual(obj.id, 89)

    def test_load_from_file(self):
        obj_list = Rectangle.load_from_file()
        self.assertEqual(len(obj_list), 0)
        self.assertIsInstance(obj_list, list)

        d = {'id': 89, 'width': 10, 'height': 4}
        obj = Rectangle.create(**d)
        obj.save_to_file([obj])

        obj_list = Rectangle.load_from_file()
        self.assertEqual(len(obj_list), 1)
        self.assertIsInstance(obj_list[0], Rectangle)


if __name__ == "__main__":
    unittest.main()
