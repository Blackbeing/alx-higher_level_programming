#!/usr/bin/python3
def is_divisible_by_2(num):
    if num % 2 == 0:
        return True
    else:
        return False


def divisible_by_2(my_list=[]):
    new_list = [is_divisible_by_2(num) for num in my_list]
    return new_list
