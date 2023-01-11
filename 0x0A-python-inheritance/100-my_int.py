#!/usr/bin/python3
"""
This module shows operator overidding, inverts __eq__ and __ne__ methods
>>> MyInt(2) == 2
False
"""


class MyInt(int):
    """
    MyInt class inherits from int, inverts __eq__ and __ne__ methods
    """
    def __eq__(self, value):
        """
        Equality operator ==

        Args:
            value (int): int arg
        """
        return super().__ne__(value)

        """
        Not equal operator !=

        Args:
            value (int): int arg
        """
    def __ne__(self, value):
        return super().__eq__(value)
