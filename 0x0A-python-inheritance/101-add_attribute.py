#!/usr/bin/python3

"""
This module defines add_attribute function, adds object attribute
>>> add_attribute(MyClass(), "name", "first_name")
"""


def add_attribute(obj, key, value):
    """
    Add attribute to object

    Args:
        key (str): str argument
        value (any): python object
    """
    if "__dict__" in dir(obj):
        obj.__dict__[key] = value
    else:
        raise TypeError("can't add new attribute")
