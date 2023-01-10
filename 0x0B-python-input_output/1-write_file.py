#!/usr/bin/python3
"""
This module defines function that writes text to a file
>>> write_file("my_text_1.txt", "It is 2023")
"""


def write_file(filename="", text=""):
    """
    Writes text to a file

    Args:
        filename: Path-like object or string to file
        text (str): text to write to file
    """
    with open(filename, 'w', encoding='utf-8') as fd:
        fwrite = fd.write(text)

    return fwrite
