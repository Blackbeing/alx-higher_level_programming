#!/usr/bin/python3
"""
This is the "add_integer" module
It supplies one function to add two int or floats. Example
>>> add_integer(1, 4)
"""


def add_integer(a, b=98):
    """ Return sum of two integers
    Type casts floats value to integer
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
