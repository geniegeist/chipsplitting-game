import numpy as np
from . import utils
from .hyperfield_vector import HyperfieldVector


class HyperfieldLinearForm:
    def __init__(self, support_pos: list[bool], support_neg: list[bool]):
        """
        A linear form in a hyperfield is just a sum of x_ij whose coefficients are either 1 or -1.

        :param support_pos: A list of boolean values that represent the positive support.
        :param support_neg: A list of boolean values that represent the negative support.
        """

        self.support_pos = np.array(support_pos)
        self.support_neg = np.array(support_neg)

    @property
    def degree(self):
        return int(-1.5 + np.sqrt(0.25 + 2 * self.support_pos.size))

    def __repr__(self) -> str:
        return f"HyperfieldLinearForm(positive support: {self.support_pos}, negative support: {self.support_neg})"

    def __str__(self) -> str:
        txt = ""
        for len_row, row_index in enumerate(range(self.degree, -1, -1)):
            for col_index in range(len_row + 1):
                pos_val = self.support_pos[utils.get_array_index(col_index, row_index)]
                neg_val = self.support_neg[utils.get_array_index(col_index, row_index)]
                val = "+" if pos_val else "-" if neg_val else "."
                txt += f"{''.join([' '] * (4 - len(val))) + val} "
            txt += "\n"
        return txt

    def __call__(self, v: HyperfieldVector):
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
