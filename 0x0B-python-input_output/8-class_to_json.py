#!/usr/bin/python3
"""
This module provides class_to_json function
>>> class_to_json(MyClassInstance)
"""


def class_to_json(obj):
    """
    Convert class to serializable json object

    Args:
        obj: Instance of class

    Returns:
        dictionary obj to be serialized
    """
    attr = {k: obj.__getattribute__(k) for k in dir(obj) if (
        not k.startswith("__") and isinstance(
            obj.__getattribute__(k), (list, str, bool, int, dict)))}

    return attr
