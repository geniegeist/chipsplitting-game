import numpy as np
from .linear_form import HyperfieldLinearForm


class HyperfieldContractionForm(HyperfieldLinearForm):
    def __init__(self, support_pos: list[bool], support_neg: list[bool]):
        """
        A linear form in a hyperfield is just a sum of x_ij whose coefficients are either 1 or -1.

        :param support_pos: A list of boolean values that represent the positive support.
        :param support_neg: A list of boolean values that represent the negative support.
        """
        assert len(support_pos) == 64, "Support must have 64 elements."
        assert len(support_neg) == 64, "Support must have 64 elements."

        self.support_pos = np.array(support_pos)
        self.support_neg = np.array(support_neg)

    def __getitem__(self, key):
        return self.values[key]

    def __repr__(self) -> str:
        return f"HyperfieldContractionForm(positive support: {self.support_pos}, negative support: {self.support_neg})"

    def __str__(self) -> str:
        return f"HyperfieldContractionForm(positive support: {self.support_pos}, negative support: {self.support_neg})"

    def __call__(self, v):
        for x in v[self.support_pos | self.support_neg]:
            if np.isnan(x):
                return np.nan

        has_pos, has_neg = False, False

        for x in v[self.support_pos]:
            if x > 0:
                has_pos = True
            elif x < 0:
                has_neg = True
            if has_neg and has_pos:
                return np.nan

        for x in v[self.support_neg]:
            if x > 0:
                has_neg = True
            elif x < 0:
                has_pos = True
            if has_neg and has_pos:
                return np.nan

        if has_neg and has_pos:
            return np.nan
        if has_neg:
            return -1
        elif has_pos:
            return 1
        return 0

    def to_indices(self, variable):
        """
        Converts a variable to an index in the contraction form.
        For example: x11 -> 5
        """
        base = 0
        offset = 0
        first_char = variable[0]
        if first_char == "x":
            base = 0
            second_char = variable[1]
            third_char = variable[2]
            offset = int(second_char) * 4 + int(third_char)
            pass
        elif first_char == "y":
            base = 16
            second_char = variable[1]
            third_char = variable[2]
            offset = int(second_char) * 4 + int(third_char)
            pass
        elif first_char == "z":
            base = 32
            second_char = variable[1]
            third_char = variable[2]
            offset = int(second_char) * 4 + int(third_char)
            pass
        elif first_char == "b":
            base = 48
            second_char = variable[1]
            offset = int(second_char)
            pass
        elif first_char == "c":
            base = 52
            second_char = variable[1]
            offset = int(second_char)
            pass
        elif first_char == "d":
            base = 56
            second_char = variable[1]
            offset = int(second_char) * 4 + int(variable[2])
            pass
        else:
            raise Exception(f"Invalid variable {variable}")
        return base + offset
