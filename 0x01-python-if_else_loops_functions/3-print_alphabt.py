#!/usr/bin/python3
for i in range(97, 97+26):
    if not chr(i) in ["q", "e"]:
        print("{:c}".format(i), end="")
