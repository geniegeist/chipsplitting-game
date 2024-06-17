"""
Module contains general linear forms.
"""

import numpy as np
from numpy._typing import NDArray

from chipsplitting.base.base_linear_form import BaseLinearForm

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
