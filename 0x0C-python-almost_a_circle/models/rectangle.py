#!/usr/bin/python3
"""
This module defines Rectangle class
>>> Rectangle(10, 2, 0, 0, 12)
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base class

    __init__ initializes Rectangle object

    Args:
        width (int): Width of rectangle
        height (int): Height of rectangle
        x (int): x variable
        y (int): y variable
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.validate_all(width=width, height=height, x=x, y=y)
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_x(value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_y(value)
        self.__y = value

    def validate_width(self, width):
        """
        validate width attribute

        Args:
            Width (int): Width of rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

    def validate_height(self, height):
        """
        validate height attribute

        Args:
            height (int): height of rectangle
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

    def validate_x(self, x):
        """
        validate x attribute

        Args:
            x (int): x of rectangle
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

    def validate_y(self, y):
        """
        validate y attribute

        Args:
            y (int): y of rectangle
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

    def validate_all(self, width, height, x, y):
        """
        Runs all validators, wrapper

        Args:
            width (int): width variable
            height (int): height variable
            x (int): x variable
            y (int): y variable
        """
        self.validate_width(width)
        self.validate_height(height)
        self.validate_x(x)
        self.validate_y(y)

    def area(self):
        """
        Calculate area of rectangle

        Returns:
            int, area of rectangle
        """
        return self.__width * self.__height
