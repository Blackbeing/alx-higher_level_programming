#!/usr/bin/python3

def uppercase(str):
    new_string = ""
    for idx, c in enumerate(str):
        if ord(c) >= 97 and ord(c) <= 122:
            new_string += chr(ord(c) - 32)
        else:
            new_string += c
    print("{}".format(new_string))
