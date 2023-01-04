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
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.validate_width(width)
        self.validate_height(height)

        self.__width = width
        self.__height = height

        self.__class__.number_of_instances += 1

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

    def area(self):
        """Get area of rectangle object
        Returns:
            int: The area of rectangle object
        """
        return self.__height * self.__width

    def perimeter(self):
        """Get perimeter of rectangle object
        Returns:
            int: The perimeter of rectangle object
        """
        if (self.__height == 0 or self.__width == 0):
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """ Print rectangle using #.
        """
        width = self.__width
        height = self.__height
        rv = ""

        if width == 0 or height == 0:
            return ""

        for _ in range(0, height):
            for _ in range(0, width):
                rv += "#"
            rv += '\n'
        rv = rv[:-1]  # Remove last new line character
        return rv

    def __repr__(self):
        """
        Print string representaion of rectangle
        Can be used to create new instance using eval()
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        print string when instance is deleted
        """
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1
