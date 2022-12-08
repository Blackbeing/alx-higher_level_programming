#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    exists = [key for key in a_dictionary if a_dictionary[key] == value]
    [a_dictionary.pop(key) for key in exists]
    return a_dictionary
