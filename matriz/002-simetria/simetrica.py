import sympy as sp

A = sp.Matrix([[3, 1, 2],
                    [1, 4, 3],
                    [2, 3, 5]])
A_transposta = A.transpose()

print(f"A é simétrica: {A == A_transposta}")

B = sp.Matrix([[7, 9, 1],
                    [6, 3, 4],
                    [3, 3, 8]])
B_transposta = B.transpose()

print(f"B é simétrica: {B == B_transposta}")
