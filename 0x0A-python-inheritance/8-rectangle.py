#!/usr/bin/python3
"""
This module defines an BaseGeometry class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines rectangle, a subclass of BaseGeometry

    __init__ method initializes a rectangle object by defining it's

    Args:
        width (int): width of rectangle
        height (int): height of rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
