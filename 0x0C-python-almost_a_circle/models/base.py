#!/usr/bin/python3
"""
This module provides the Base class for project classes
"""


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