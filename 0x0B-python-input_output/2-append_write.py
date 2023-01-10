#!/usr/bin/python3
"""
This module defines function that appends text to a file
>>> write_file("my_text_1.txt", "It is 2023")
"""


def append_write(filename="", text=""):
    """
    Append text to a file

    Args:
        filename: Path-like object or string to file
        text (str): text to append to file
    """
    with open(filename, 'a', encoding='utf-8') as fd:
        fwrite = fd.write(text)

    return fwrite
