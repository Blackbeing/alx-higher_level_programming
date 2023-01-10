#!/usr/bin/python3
"""
This module provides the student class
"""


class Student:
    """
    __init__ initializes Student class

    Args:
        first_name (str): First name
        last_name (str): Last name
        age (int): Age of student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Convert instance to serializable json object

        Args:
            obj: Instance of class

        Returns:
            dictionary obj to be serialized
        """
        attr = {k: self.__getattribute__(k) for k in dir(self) if (
            not k.startswith("__") and isinstance(
                self.__getattribute__(k), (list, str, bool, int, dict)))}

        if not attrs:
            return attr
        return dict(filter(lambda x: x[0] in attrs, attr.items()))

    def reload_from_json(self, json):
        """
        Update attributes of instance

        Args:
            json (dict): Update dict object
        """
        self.__dict__.update(json)
