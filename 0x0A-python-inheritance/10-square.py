#!/usr/bin/python3
"""
This module defines an BaseGeometry class
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class

    __init__ method initializes a square object by defining it's size.

    Args:
        size (int): Size of side of square
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self._size = size
        super().__init__(self._size, self._size)
