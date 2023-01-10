#!/usr/bin/python3
"""
This module defines an BaseGeometry class
"""


class BaseGeometry:
    """
    BaseGeometry class to define geometry objects
    """

    def area(self):
        """
        Not yet implemented method
        Raises Exception if called
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate integer value

        Args:
            name (str): str argument
            value (int): int arguement

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to zero
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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

        self._width = width
        self._height = height

    def area(self):
        """
        Gets area of rectangle

        Returns:
            Area of rectangle
        """
        return self._width * self._height

    def __str__(self):
        """
        Get string representation of rectangle

        Returns:
            string representation of rectangle
        """
        return f"[Rectangle] {self._width}/{self._height}"
