#!/usr/bin/python3

"""
This module defines inherits_from
>>> inherits_from(1, int.__name__)
True
"""


def inherits_from(obj, a_class):
    """
    Test if object inhertits from a class

    Args:
        obj: object
        a_class: Class
    Return:
        True or false
    """
    if isinstance(obj, a_class) and not issubclass(a_class, obj.__class__):
        return True
    return False
