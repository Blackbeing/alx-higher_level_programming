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
    def __init__(self, size=0, position=(0, 0)):
        self.validate_size(size)
        self.validate_pos(position)

        self.__size = size
        self.__position = position

    def area(self):
        """Get area of square object
        Returns:
            int: The area of square object
        """
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        validate_size(value)
        self.__size = value

    def validate_size(self, size):
        print(size)
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def validate_pos(self, position):
        if (
            not isinstance(position, tuple)
            or not len(position) == 2
            or not all([isinstance(x, int) for x in position])
            or not all([x >= 0 for x in position])
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        validate_pos(value)
        self.__position = value

    def my_print(self):
        """ Print square using #.
        """
        side = self.__size
        pos = self.__position

        if not side:
            print()

        else:
            for height in range(0, side):
                for spaces in range(pos[0]):
                    print("_", end="")
                for width in range(0, side):
                    print("#", end="")
                print()
