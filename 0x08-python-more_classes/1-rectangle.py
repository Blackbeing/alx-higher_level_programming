#!/usr/bin/python3
"""Class definition for Rectangle

Defines class objects to be used in ALX assignments.
"""


class Rectangle:
    """Rectangle class

    __init__ method initializes a rectangle object by defining it's
    height and width.

    Args:
        size (int): Size of square
    """

    def __init__(self, width=0, height=0):
        self.validate_width(width)
        self.validate_height(height)

        self.__width = width
        self.__height = height

    def validate_width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

    def validate_height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_width(value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_height(value)
        self.__height = value
