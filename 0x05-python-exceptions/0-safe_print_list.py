#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for _ in my_list[:x]:
            count += 1
            print(_, end="")
        print()
    except Exception as error:
        print(error)
    return count
