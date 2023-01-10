#!/usr/bin/python3
"""
This module defines function that save object to file
>>> save_to_json_file([1, 3, 4], "my_list_0.txt")
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Save object to file in json form

    Args:
        my_obj: Object
        filename: Path-like object or string
    """
    with open(filename, "w", encoding="utf-8") as fd:
        json.dump(my_obj, fd)
