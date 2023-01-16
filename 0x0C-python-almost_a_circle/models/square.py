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

    @property
    def size(self):
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        self.validate_width(value)
        self._Rectangle__width = value
        self._Rectangle__height = value

    def update(self, *args, **kwargs):
        """
        Update object instance attributes

        Args:
            args: non-keyword args
            kwargs: keyword args
        """
        attr_list = ["id", "size", "x", "y"]
        if args and args is not None:
            for idx, attr in enumerate(args):
                setattr(self, attr_list[idx], attr)
        else:
            for k, v in kwargs.items():
                if k in attr_list:
                    setattr(self, k, v)

    def to_dictionary(self):
        """
        Convert instance to dict object

        Returns:
            dictionary with object attributes
        """
        attr_list = ["id", "size", "x", "y"]

        attr = {k: self.__getattribute__(k) for k in dir(self) if (
            k in attr_list
            and not k.startswith("__")
            and not k.startswith("_")
            and isinstance(
                self.__getattribute__(k), (list, str, bool, int, dict)))}
        return attr
