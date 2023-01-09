#!/usr/bin/python3
"""
This module defines is_same_class
>>> is_same_class(1, int.__name__)
True
"""


def is_same_class(obj, a_class):
    """
    Test if object belongs to a class

    Args:
        obj: object
        a_class: Class
    Return:
        True or false
    """
    if type(obj) == a_class:
        return True
    return False
