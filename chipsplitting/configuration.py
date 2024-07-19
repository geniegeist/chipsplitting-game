"""
This module contains all the methods related to 
chipsplitting configurations.
"""

from typing import Union

from .utils import gauss, get_array_index, to_coordinate


def initial_config() -> dict:
    """
    Return the initial configuration of the chipsplitting game.
    """
    return {}


def print_config(support: list[Union[int, tuple]], values: list[int], degree: int):
    """
    Print the chipsplitting configuration in a triangular form.

    :param support: A list of integers representing the support of the configuration.
    :param degree: The degree of the chipsplitting game.
    """

    if not support:
        print("Empty configuration.")
        return

    if isinstance(support[0], tuple):
        support = [get_array_index(col, row) for col, row in support]

    for row in range(degree, -1, -1):
        row_str = ""
        for col in range(degree + 1):
            if col + row > degree:
                continue
            index = get_array_index(col, row)
            support_index = support.index(index) if index in support else None

            if support_index is not None:
                value = str(round(values[support_index], 2))
                row_str += f"{' ' * (max(8 - len(value), 0))}{value}"
            else:
                row_str += " " * 7 + "."
        print(row_str)


def reflect_support(support: list[Union[int, tuple]]) -> tuple[int]:
    """
    Reflect the chipsplitting configuration along the diagonal.
    """
    reflected_support = []
    for i in support:
        coord = to_coordinate(i)
        reflected_support.append(get_array_index(coord[1], coord[0]))
    return tuple(reflected_support)


def reflect_config(
    support: list[Union[int, tuple]], values: list[int]
) -> tuple[tuple[int], list[int]]:
    """
    Reflect the chipsplitting configuration along the diagonal.
    """
    reflected_support = reflect_support(support)
    return reflected_support, values
