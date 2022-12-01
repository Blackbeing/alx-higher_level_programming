#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = len(argv)
    ops = {'+': add, '-': sub, '*': mul, '/': div}

    if argc != 3:  # including program 0
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(argv[0])
    op = argv[1]
    b = int(argv[2])

    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{:d} {} {:d} = {:d}".format(a, op, b, ops[op](a, b)))
