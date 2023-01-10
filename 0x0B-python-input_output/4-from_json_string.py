#!/usr/bin/python3
"""
This module defines function to convert json string to an object
>>> from_json_string("{'a': 1, 'b':2}")
"""
import json


def from_json_string(my_str):
    """
    Object from json string

    Args:
        my_str: Json string

    Returns:
        Object
    """
    return json.loads(my_str)
