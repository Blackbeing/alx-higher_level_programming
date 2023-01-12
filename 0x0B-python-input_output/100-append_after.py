#!/usr/bin/python3
"""
This module provides append_after function, adds string after occurence of str
>>> append_after("file.txt", "Python", "Is so cool")
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Append string after occurence of string

    Args:
        filename (str|path): path-like string or path object
        search_string (str): str arg
        new_string (str): str arg

    """
    new_list = []
    with open(filename, 'r+', encoding="utf-8") as fd:
        line = fd.readline()
        while line != "":
            new_list.append(line)
            if search_string in line:
                new_list.append(f"{new_string}")
            line = fd.readline()

    # with open(filename, 'w', encoding="utf-8") as fd:
        fd.seek(0)
        fd.write("".join(new_list))
