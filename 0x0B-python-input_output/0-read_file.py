#!/usr/bin/python3
"""
This module defines function to read a file
>>> read_file("my_file_0.txt")
"""


def read_file(filename=""):
    """
    Function that reads UTF-8 file

    Args:
        filename: Path-like object or str to file
    """

    with open(filename, 'r', encoding="utf-8") as fd:
        print(fd.read(), end="")
