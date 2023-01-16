#!/usr/bin/python3
"""
This module defines Square class
>>> Square(10)
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle class

    __init__ initializes Square object

    Args:
        size (int): length/width of square
        x (int): x variable
        y (int): y variable
        id (int): id of square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(x=x, y=y, id=id, width=size, height=size)

    def __str__(self):
        """
        Return string representation of Square

        Returns:
            string
        """
        return f"""[Square] ({self.id}) {self.x}/{self.y} \
- {self.width}"""
