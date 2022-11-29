#!/usr/bin/python3

for i in range(0, 99+1):
    if i == 99:
        print("{:0>2}".format(i))
    else:
        print("{:0>2}, ".format(i), end="")
