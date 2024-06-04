import numpy as np
from . import utils


class HyperfieldVector:
    """
    A hyperfield vector is a vector that only contains -1, 0 and 1 values.

    :param values: A list of values that represent the vector. It can be a 2D triangle or a flat list.
    """

    def __init__(self, values: list):
        if len(values) == 0:
            self.values = np.array([])
        elif isinstance(values[0], list):
            flat = np.full(len(np.concatenate(values)), 0)
            for r, row in enumerate(values):
                for c, val in enumerate(row):
                    flat[utils.get_array_index(c, len(values) - 1 - r)] = val
                self.values = np.array(flat)
        else:
            self.values = np.array(values)

        for x in self.values:
            assert x in [
                -1,
                0,
                1,
            ], "Hyperfield vector may only contain -1, 0 and 1 values."

    @property
    def degree(self):
        return int(-1.5 + np.sqrt(0.25 + 2 * self.values.size))

    @property
    def is_valid(self):
        if self.values[0] > 0:
            return False
        for v in self.values[1:]:
            if v < 0:
                return False
        return True

    def __getitem__(self, key):
        return self.values[key]

    def __repr__(self) -> str:
        return f"HyperfieldVector({self.values})"

    def __str__(self) -> str:
        txt = ""
        for len_row, row_index in enumerate(range(self.degree, -1, -1)):
            for col_index in range(len_row + 1):
                val = str(self.values[utils.get_array_index(col_index, row_index)])
                txt += f"{''.join([' '] * (4 - len(val))) + val} "
            txt += "\n"
        return txt

    def __lor__(self, other):
        return self.values | other
