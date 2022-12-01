#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # for this task only
    argc = len(argv)  # for this task only

    if argc == 1:
        print("{:d} argument:".format(argc))
    elif argc == 0 or argc > 1:
        print("{:d} arguments{}".format(argc, ':' if argc > 0 else '.'))

    for idx, arg in enumerate(argv):
        print("{:d}: {}".format(idx+1, arg))
