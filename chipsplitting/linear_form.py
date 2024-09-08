"""
Module contains general linear forms.
"""

import numpy as np
from numpy._typing import NDArray

from chipsplitting.base import BaseLinearForm
from chipsplitting.hyperfield.hyperfield_linear_form import HyperfieldLinearForm

from .utils import gauss
from .utils.coordinate_transformation import get_array_index


class LinearForm(BaseLinearForm):
    """
    Class for general linear forms
    """

    def __init__(self, support_pos: NDArray[np.int_], support_neg: NDArray[np.int_]):
        """
        A linear form is just a sum of x_ij.

        """

        self._support_pos = np.array(support_pos)
        self._support_neg = np.array(support_neg)

    @classmethod
    def zero(cls, degree: int):
        """
        Returns a zero linear form of the given degree.
        """
        return cls(np.array([0] * gauss(degree + 1)), np.array([0] * gauss(degree + 1)))

    @property
    def support_neg(self) -> NDArray[np.int_]:
        return self._support_neg

    @property
    def support_pos(self) -> NDArray[np.int_]:
        return self._support_pos

    @property
    def degree(self):
        """
        The degree of the linear form. It is defined as argmax i+j,
        where (i,j) is contained in the support
        """

        return int(-1.5 + np.sqrt(0.25 + 2 * self.support_pos.size))

    def __repr__(self) -> str:
        return (
            f"LinearForm(positive support: {self.support_pos}, "
            f"negative support: {self.support_neg})"
        )

    def __str__(self) -> str:
        txt = ""
        for len_row, row_index in enumerate(range(self.degree, -1, -1)):
            for col_index in range(len_row + 1):
                pos_val = self.support_pos[get_array_index(col_index, row_index)]
                neg_val = self.support_neg[get_array_index(col_index, row_index)]
                val = (
                    str(pos_val)
                    if pos_val > 0
                    else f"-{str(neg_val)}" if neg_val > 0 else "."
                )
                txt += f"{''.join([' '] * (4 - len(val))) + val} "
            txt += "\n"
        return txt

    def __call__(self, v):
        pos = 0
        neg = 0

        for i in range(self.support_pos.size):
            pos += self.support_pos[i] * v[i]

        for i in range(self.support_neg.size):
            neg += self.support_neg[i] * v[i]

        return pos - neg

    def __eq__(self, other):
        return np.all(self.support_pos == other.support_pos) and np.all(
            self.support_neg == other.support_neg
        )

    def __add__(self, other):
        support_pos = np.array([0] * gauss(self.degree + 1))
        support_neg = np.array([0] * gauss(self.degree + 1))

        for i in range(support_pos.size):
            val = (
                self.support_pos[i]
                - self.support_neg[i]
                + other.support_pos[i]
                - other.support_neg[i]
            )
            if val > 0:
                support_pos[i] = val
            elif val < 0:
                support_neg[i] = -val

        return LinearForm(support_pos, support_neg)

    def __sub__(self, other):
        support_pos = np.array([0] * gauss(self.degree + 1))
        support_neg = np.array([0] * gauss(self.degree + 1))

        for i in range(support_pos.size):
            val = (
                self.support_pos[i]
                - self.support_neg[i]
                - other.support_pos[i]
                + other.support_neg[i]
            )
            if val > 0:
                support_pos[i] = val
            elif val < 0:
                support_neg[i] = -val

        return LinearForm(support_pos, support_neg)

    def to_hyperfield(self) -> HyperfieldLinearForm:
        """
        Converts the Pascal form to a hyperfield linear form.
        """
        support_pos = np.full(gauss(self.degree + 1), False)
        support_neg = np.full(gauss(self.degree + 1), False)

        for index, val in enumerate(self.support_pos):
            if val > 0:
                support_pos[index] = True

        for (
            index,
            val,
        ) in enumerate(self.support_neg):
            if val > 0:
                support_neg[index] = True

        return HyperfieldLinearForm(support_pos, support_neg)
