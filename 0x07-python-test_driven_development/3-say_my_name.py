#!/usr/bin/python3

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

    print(f"{first_name} {last_name}")
