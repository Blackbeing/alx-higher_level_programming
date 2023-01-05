#!/usr/bin/python3
"""
This module provides function to print name
>>> say_my_name("John", "Doe")
My name is John Doe
"""


def say_my_name(first_name, last_name=""):
    """
    Function to print both first and last name

    Args:
        first_name: first name string
        last_name: last name string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
