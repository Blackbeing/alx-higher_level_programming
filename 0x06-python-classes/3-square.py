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
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Get area of square object
        Returns:
            int: The area of square object
        """
        return self.__size ** 2
