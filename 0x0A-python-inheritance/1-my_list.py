#!/usr/bin/python3

"""
This module defines MyList class which inherits from list object
>>> x = MyList()
>>> x.append(2)
"""


class MyList(list):
    """
    MyList class
    Inherits from list class
    """
    def print_sorted(self):
        """
        Print sorted instance of list
        """
        print(sorted(self))
