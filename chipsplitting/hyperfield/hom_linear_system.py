"""
This module contains everything related to solving linear systems 
of homogeneous linear forms in a hyperfield.
"""

from collections import deque

import numpy as np

from .hyperfield_vector import HyperfieldVector
from .linear_form import HyperfieldLinearForm


class HyperfieldHomogeneousLinearSystem:
    """
    A system of homogeneous linear forms in a hyperfield.
    It contains a list of linear forms that we want to roots for.
    """

    def __init__(self, linear_forms: list[HyperfieldLinearForm]):
        self.linear_forms = linear_forms

        conditions = []
        for form in linear_forms:
            if form.support_pos[0]:
                cond = np.copy(form.support_pos)
                cond[0] = False
                conditions.append(form.support_pos)
            elif form.support_neg[0]:
                cond = np.copy(form.support_neg)
                cond[0] = False
                conditions.append(form.support_neg)
            elif np.any(form.support_pos) and np.any(form.support_neg):
                conditions.append(form.support_pos)
                conditions.append(form.support_neg)
        self.conditions = np.array(conditions)

    def __str__(self) -> str:
        return "\n".join(str(form) for form in self.linear_forms)

    def is_solved_by_valid(self, vector: HyperfieldVector) -> bool:
        """
        Returns true if the vector is a root of every linear form in the system.
        Vector must be valid, i.e. its negative support must be empty or may only contain zero.
        """
        assert vector.is_valid, "Vector must be valid."
        support_without_neg = np.array(vector.values, dtype=bool)
        support_without_neg[0] = False
        return bool(np.all(self.conditions.dot(support_without_neg)))

    def make_constraints(self) -> list[set[int]]:
        """
        Given the list of linear forms, compute a list constraints.
        Each constraint must be satisfied for a configuration to be considered valid.
        A configuration satisfies a constraint if and only if some component
        of the configuration is in contained in the constraint.
        """
        constraints = []
        # contains tuples of positive and negative support for each linear form
        supports = [
            (set(form.support_pos.nonzero()[0]), set(form.support_neg.nonzero()[0]))
            for form in self.linear_forms
        ]
        for pos, neg in supports:
            if 0 in pos:
                new_constr = {i for i in pos if i > 0}
                if new_constr not in constraints:
                    constraints.append(new_constr)
            elif 0 in neg:
                new_constr = {i for i in neg if i > 0}
                if new_constr not in constraints:
                    constraints.append(new_constr)
            elif len(pos) and len(neg):
                pos_constr = set(pos)
                neg_constr = set(neg)
                if pos_constr not in constraints:
                    constraints.append(pos_constr)
                if neg_constr not in constraints:
                    constraints.append(neg_constr)
            else:
                raise UnsolvableSystemException("Unsolvable system of linear forms")

        to_remove = []
        for c in constraints:
            for d in constraints:
                if c == d:
                    continue
                intersected = c.intersection(d)
                if len(intersected) == len(c):
                    to_remove.append(d)
                elif len(intersected) == len(d):
                    to_remove.append(c)

        return [x for x in constraints if x not in to_remove]

    def quick_solve(self, support_size: int) -> list[list[int]]:
        """
        Solves the system by searching for all possible solutions with a given support size.
        Use quick_solve_loop for faster results.
        """

        def to_tuple(a):
            a = a.copy()
            a.sort()
            return tuple(a)

        visited = set()

        solutions = []
        accu = []
        constraints = self.make_constraints()

        def dfs(constr_index):
            if to_tuple(accu) in visited:
                return

            # went through all constraints
            if constr_index == len(constraints):
                if len(accu) == support_size:
                    solutions.append(accu.copy())
                visited.add(to_tuple(accu))
                return

            constr = constraints[constr_index]

            satisfies_constr = False
            for i in accu:
                if i in constr:
                    satisfies_constr = True
                    break

            if satisfies_constr:
                dfs(constr_index + 1)
            elif len(accu) < support_size:
                # accumulator does not satisfy constraint and it is not full
                # hence we can add an index to the accumulator so that it satisfies the constraint
                for i in [
                    j for j in constr if j not in accu
                ]:  # we don't want to add duplicate indices to the accumulator
                    accu.append(i)
                    dfs(constr_index + 1)
                    accu.pop()
            else:
                # found an invalid solution
                # remember this invalid solution we don't do repeated work
                visited.add(to_tuple(accu))

        dfs(0)

        return solutions

    def quick_solve_loop(self, support_size: int):
        """
        The fastest way to find roots of the system.
        """
        constraints = self.make_constraints()
        constraints.sort(key=len)
        queue = deque([tuple()])

        for constr in constraints:
            for _ in range(len(queue)):
                conf = queue.popleft()

                satisfy = False
                for i in conf:
                    if i in constr:
                        satisfy = True
                        break

                if satisfy:
                    queue.append(conf)
                elif len(conf) < support_size:
                    for j in constr:
                        queue.append((*conf, j))

        return list({tuple(sorted(list(x))) for x in queue})


class UnsolvableSystemException(Exception):
    """
    The system is not solvable.
    """
