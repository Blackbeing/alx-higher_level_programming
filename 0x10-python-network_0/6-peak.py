#!/usr/bin/python3
"""
This module finds the peak of a list and returns it's values.
If list is empty, returns None.
>>> find_peak([1, 2, 4, 6, 3])
"""


def find_peak(list_of_integers):
    """
    Find a peak in an unsorted list
    Peak:  Neigbouring elements are less than or equal to
    """
    if not list_of_integers:
        return None

    # Get index of middle element
    m = len(list_of_integers) // 2

    # If we reach most left end, return first element
    if m == 0:
        return list_of_integers[m]

    # if list has two objects return the biggest
    if m == 1:
        return max(list_of_integers)

    # if m-1 elem is gte to m, recursively call function with left array
    if list_of_integers[m - 1] >= list_of_integers[m]:
        return find_peak(list_of_integers[:m])

    # if m-1 elem is gte to m, recursively call function with right array
    elif list_of_integers[m + 1] >= list_of_integers[m]:
        # print(m)
        return find_peak(list_of_integers[m:])

    # Otherwise, return element
    else:
        return list_of_integers[m]
