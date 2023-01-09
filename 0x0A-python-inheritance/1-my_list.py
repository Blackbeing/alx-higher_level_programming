#!/usr/bin/python3

"""
This module defines MyList class which inherits from list object
>>> x = MyList()
>>> x.append(2)
"""


class MyList(list):
    """
    MyList class

    __init__ method Initialize MyList object
    """
    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        """
        Print sorted instance of list
        """
        print(sorted(self))
