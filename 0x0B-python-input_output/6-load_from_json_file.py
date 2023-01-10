#!/usr/bin/python3
"""
This module defines function that loads object from file
>>> load_from_json_file("my_list_0.txt")
"""
import json


def load_from_json_file(filename):
    """
    Load object from file

    Args:
        filename: Path-like object or string

    Returns:
        Python object
    """
    with open(filename, "r", encoding="utf-8") as fd:
        obj = json.load(fd)
    return obj
