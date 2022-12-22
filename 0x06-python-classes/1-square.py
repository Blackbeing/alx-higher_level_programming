#!/usr/bin/python3
"""Class definition for ALX assignments

Defines class objects to be used in assignments.
"""


class Square:
    """Square class

    __init__ method initializes a square object by defining it's size.

    Args:
        size (int): Size of square
    """
    def __init__(self, size):
        self.__size = size
