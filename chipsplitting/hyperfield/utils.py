import math
from ..utils import gauss


def get_array_index(col, row):
    return gauss(col + row) + col


def to_coordinate(n):
    degree = int(-1.5 + math.sqrt(0.25 + 2 * n)) + 1
    s = gauss(degree)
    return (n - s, degree - n + s)


def grid_iter(degree, support_size):
    def gen(depth, upper_bound):
        if depth == 0:
            yield ()
        else:
            for i in range(1, upper_bound):
                for rest in gen(depth - 1, i):
                    yield (i,) + rest

    for d in range(degree + 1):
        diag = get_array_index(d, degree - d)
        for rest in gen(support_size - 1, diag):
            yield (diag,) + rest
