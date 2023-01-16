#!/usr/bin/python3
"""
This module provides the Base class for project classes
"""
import json
from pathlib import Path


class Base:
    """
    Base class for other project classes

    __init__ initializes object with id attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts list of dicts to json string

        Args:
            list_dictionaries (list): list of dicts

        Returns:
            Json string
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write json string to file

        Args:
            list_objs: list of instances
        """

        file_name = f"{cls.__name__}.json"
        if list_objs is None:
            to_write = cls.to_json_string()
        else:
            to_write = cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs])

        with open(file_name, 'w', encoding='utf-8') as fd:
            fd.write(to_write)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert json string to list

        Args:
            json_string (str): json string

        Returns:
            list of dicts
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create class instance from dictionary

        Args:
            dictionary (dict): dict

        Returns:
            cls instance object
        """

        # Rectangle(width, height)
        # Square(size, x)

        if cls.__name__ == "Rectangle":
            dummy_obj = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_obj = cls(1)

        dummy_obj.update(**dictionary)
        return dummy_obj

    @classmethod
    def load_from_file(cls):
        """
        Load instance from file
        """
        file_name = f"{cls.__name__}.json"
        if not Path(file_name).exists():
            return []

        ret_value = []
        with open(file_name, 'r') as fd:
            obj_list = cls.from_json_string(fd.read())
            for obj in obj_list:
                ret_value.append(cls.create(**obj))

        return ret_value
