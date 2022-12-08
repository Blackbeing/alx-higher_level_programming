#!/usr/bin/python3
def prod(iterable):
    num = 1
    for i in iterable:
        num *= i
    return num


def weight_average(my_list=[]):
    if not my_list:
        return 0

    t = list(map(lambda x: (prod(x), x[1]), my_list))
    total_scores, total_weight = zip(*t)
    return sum(total_scores) / sum(total_weight)
