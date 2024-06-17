"""
Some utility functions.
"""

import math
from typing import Union

import numpy as np


def ncr(n: int, r: int):
    """
    Compute the binomial coefficient n choose r.
    """
    f = math.factorial
    return f(n) // f(r) // f(n - r)


def det(matrix):
    """
    Compute the determinant of a matrix.
    """
    return np.linalg.det(matrix)


def print_matrix(matrix: Union[np.ndarray, list[list[int]]]):
    """
    Print a matrix.
    """
    for row in matrix:
        for val in row:
            val = str(val)
            print(f"{''.join([' '] * (4 - len(val))) + val}", end=" ")
        print("")


def phi_coefficients(degree: int, unit: int) -> list[list[int]]:
    """
    Compute the coefficients of the diagonal Pascal equations

    :param degree: The degree of the Pascal form.
    :param unit: The unit of the Pascal form.
    :return: A list of coefficients as a 2D list.
    """
    coefficients = []
    for col in range(degree + 1):
        rows = []
        for row in range(degree + 1 - col):
            if unit - col >= 0 and degree - col - row >= unit - col:
                rows.append(ncr(degree - col - row, unit - col))
            else:
                rows.append(0)
        coefficients.append(rows)
    return coefficients


def pairing_matrix(
    degree: int, units: list[int], support: list[list[int]]
) -> list[list[int]]:
    """
    Compute the pairing matrix.
    """
    assert len(units) == len(support), "E and S must have same length"
    p_matrix = []  # pairing matrix to return

    for a in units:
        phi_coeff = phi_coefficients(degree, a)
        row = [phi_coeff[i][j] for i, j in support]
        p_matrix.append(row)

    return p_matrix
