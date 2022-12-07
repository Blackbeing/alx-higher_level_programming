#!/usr/bin/python3
def best_score(a_dictionary):
    # a_dictionary.items() -- list of tuples [("john", 12), ('Bob': 14)]
    # lambda student:student[1] -- use student[1] ie, score as sorting key
    # in ascending order
    # select last element, highest value
    if not a_dictionary:
        return
    try:
        sorted_dict = sorted(a_dictionary.items(), key=lambda stud: stud[1])
    except Exception:
        return

    highest_key = sorted_dict[-1][0]
    return highest_key
