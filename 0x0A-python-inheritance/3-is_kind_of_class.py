#!/usr/bin/python3
"""
This module defines is_kind_of_class
>>> is_kind_of_class(1, int.__name__)
True
"""


def is_kind_of_class(obj, a_class):
    """
    Test if object belongs to a class or super class

    Args:
        obj: object
        a_class: Class
    Return:
        True or false
    """
    if isinstance(obj, a_class):
        return True
    return False
