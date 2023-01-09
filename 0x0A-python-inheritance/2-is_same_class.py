#!/usr/bin/python3
"""
This module defines is_same_class
>>> is_same_class(1, int.__name__)
True
"""


def is_same_class(obj, a_class):
    if type(obj) == a_class:
        return True
    return False
