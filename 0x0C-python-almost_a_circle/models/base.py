#!/usr/bin/python3
"""
This module provides the Base class for project classes
"""
import json


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
