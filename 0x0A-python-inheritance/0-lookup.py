#!/usr/bin/python3
"""
This module defines lookup method. It returns available methods and attrs
Example:
>>> lookup(MyClass)
"""


def lookup(obj):
    """
    Return available methods and attributes
    Args:
        obj: Object
    """
    return (dir(obj))
