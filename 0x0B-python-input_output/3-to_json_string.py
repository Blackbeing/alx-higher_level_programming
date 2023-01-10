#!/usr/bin/python3
"""
This module defines function to jsonify an object
>>> to_json_string({'a': 1, 'b':2})
"""
import json


def to_json_string(my_obj):
    """
    Jsonify an object

    Args:
        my_obj: Object to jsonify

    Returns:
        Json string
    """
    return json.dumps(my_obj)
