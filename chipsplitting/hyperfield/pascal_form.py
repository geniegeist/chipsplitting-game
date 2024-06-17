"""
Module containing the Pascal form class for hyperfields
"""

import numpy as np

from . import utils
from .contraction_form import HyperfieldContractionForm
from .linear_form import HyperfieldLinearForm


class HyperfieldPascalForm(HyperfieldLinearForm):
    """
    Class for Pascal forms of hyperfields.
    """

    def __init__(self, degree: int, mode: str, unit: int):
        support_pos = np.full(utils.gauss(degree + 1), False)
        support_neg = np.full(utils.gauss(degree + 1), False)
        self._mode = mode

        if mode == "diagonal" or mode == "diag":
            for x in range(unit + 1):
                for y in range(degree - unit, -1, -1):
                    support_pos[utils.get_array_index(x, y)] = True
        elif mode == "column" or mode == "col":
            for j in range(unit + 1):
                for i in range(unit - j, degree - j + 1):
                    if (unit - j) % 2 == 0:
                        support_pos[utils.get_array_index(i, j)] = True
                    else:
                        support_neg[utils.get_array_index(i, j)] = True
        elif mode == "row":
            for j in range(unit + 1):
                for i in range(unit - j, degree - j + 1):
                    if (unit - j) % 2 == 0:
                        support_pos[utils.get_array_index(j, i)] = True
                    else:
                        support_neg[utils.get_array_index(j, i)] = True
        else:
            raise ValueError("Mode must be 'diagonal', 'column' or 'row'.")

        super().__init__(support_pos, support_neg)

    @property
    def mode(self):
        return self._mode

    def contract(self):
        """
        Converts the Pascal form to a contraction form.
        """
        assert self.degree >= 12, "Degree must be at least 12"

        support_pos = np.full(64, False)
        support_neg = np.full(64, False)

        x_coordinates = [0, 1, 3, 6, 2, 4, 7, 11, 5, 8, 12, 17, 9, 13, 18, 24]
        y_coordinates = [
            utils.gauss(self.degree - 3 + j) + i for i in range(4) for j in range(4)
        ]
        z_coordinates = [
            utils.gauss(self.degree - 3 + i) + self.degree - 3 + i - j
            for i in range(4)
            for j in range(4)
        ]
        b_coordinates = [14, 19, 25, 32]
        c_coordinates = [10, 16, 23, 31]
        d0_coordinates = [utils.gauss(self.degree - i) + 4 for i in range(4)]
        d1_coordinates = [utils.gauss(self.degree - i) + 5 for i in range(4)]

        for c, i in enumerate(x_coordinates):
            index_to_update = (c // 4) * 4 + c % 4
            if self.support_pos[i]:
                support_pos[index_to_update] = True
            elif self.support_neg[i]:
                support_neg[index_to_update] = True

        for c, i in enumerate(y_coordinates):
            index_to_update = (c // 4) * 4 + c % 4 + 16
            if self.support_pos[i]:
                support_pos[index_to_update] = True
            elif self.support_neg[i]:
                support_neg[index_to_update] = True

        for c, i in enumerate(z_coordinates):
            index_to_update = (c // 4) * 4 + c % 4 + 32
            if self.support_pos[i]:
                support_pos[index_to_update] = True
            elif self.support_neg[i]:
                support_neg[index_to_update] = True

        for c, i in enumerate(b_coordinates):
            index_to_update = (c // 4) * 4 + c % 4 + 48
            if self.support_pos[i]:
                support_pos[index_to_update] = True
            elif self.support_neg[i]:
                support_neg[index_to_update] = True

        for c, i in enumerate(c_coordinates):
            index_to_update = (c // 4) * 4 + c % 4 + 52
            if self.support_pos[i]:
                support_pos[index_to_update] = True
            elif self.support_neg[i]:
                support_neg[index_to_update] = True

        for c, i in enumerate(d0_coordinates):
            index_to_update = (c // 4) * 4 + c % 4 + 56
            if self.support_pos[i]:
                support_pos[index_to_update] = True
            elif self.support_neg[i]:
                support_neg[index_to_update] = True

        for c, i in enumerate(d1_coordinates):
            index_to_update = (c // 4) * 4 + c % 4 + 60
            if self.support_pos[i]:
                support_pos[index_to_update] = True
            elif self.support_neg[i]:
                support_neg[index_to_update] = True

        return HyperfieldContractionForm(support_pos, support_neg)
