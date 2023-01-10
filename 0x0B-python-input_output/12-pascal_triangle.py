#!/usr/bin/python3
"""
This module defines pascal_triangle
>>> pascal_triangle(5)
"""


def pascal_triangle(n):
    """
    Create a list of list representing pascals triangle

    Args:
        n (int): int argument
    """

    ret_val = []
    if n <= 0:
        return ret_val

    for line in range(1, n + 1):
        C = 1
        val_list = []
        for i in range(1, line + 1):
            val_list.append(C)
            C = int(C * (line - i) / i)
        ret_val.append(val_list)
    return ret_val
