#!/usr/bin/python3

def validate_tuple(t):

    if len(t) < 2:
        t = list(t)
        t.extend([0 for _ in range(2-len(t))])
        return tuple(t)
    elif len(t) > 2:
        t = tuple(t[i] for i in range(2))
    return t


def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a = validate_tuple(tuple_a)
    tuple_b = validate_tuple(tuple_b)

    return tuple(map(sum, zip(tuple_a, tuple_b)))
