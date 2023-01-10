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
