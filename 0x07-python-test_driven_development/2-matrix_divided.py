#!/usr/bin/python3
"""
This is the matrix_divided module
It provides function to divide all matix values by a number
>>> matrix_divided([[1,2,3], [4,5,6]], 4)
"""


def matrix_divided(matrix, div):
    """
    Divides all matrix values by number
    Takes matrix and number to divide all matrices values
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        ZeroDivisionError("division by zero")

    is_list = isinstance(matrix, list)
    # ll - list of list
    is_ll = all([isinstance(row, list) for row in matrix])
    # llif - list of floats/integers
    is_llif = all([
        isinstance(col, (float, int)) for row in matrix for col in row
        ])

    if not all([is_list, is_ll, is_llif]):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
        )

    # check if all rows are of equal size
    same_size = all([len(row) == len(matrix[0]) for row in matrix])
    if not same_size:
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda x: round(x/div, 2), row)))

    return (new_matrix)
