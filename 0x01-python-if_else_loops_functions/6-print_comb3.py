#!/usr/bin/python3

for i in range(0, 9+1):
    for j in range(0, 9+1):
        if (j > i):
            print("{0}{1}".format(i, j), end="")
            if (j+i) != 17:
                print("{}".format(", "), end="")

print("{}".format(""))
