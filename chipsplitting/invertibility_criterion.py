import numpy as np
import math

def ncr(n, r):
  f = math.factorial
  return f(n) // f(r) // f(n-r)

def det(A):
  return np.linalg.det(A)

def prettyMatrix(A):
  for row in A:
      for val in row:
          val = str(val)
          print(f"{''.join([' '] * (4 - len(val))) + val}", end=" ")
      print("")

def phi_coefficients(degree, a):
    coefficients = []
    for col in range(degree + 1):
        rows = []
        for row in range(degree + 1 - col):
            if a - col >= 0 and degree - col - row >= a - col:
                rows.append(ncr(degree - col - row, a - col))
            else:
                rows.append(0)
        coefficients.append(rows)
    return coefficients

def pairing_matrix(degree, E, S):
    assert len(E) == len(S), "E and S must have same length"
    A = []

    for a in E:
        phi_coeff = phi_coefficients(degree, a)
        row = [phi_coeff[i][j] for i,j in S]
        A.append(row)
    
    return A