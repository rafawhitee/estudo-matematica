import sympy as sp

A = sp.Matrix([[0, 3],
                    [-3, 0]])
A_oposta = -A
A_transposta = A.transpose()

print(f"A é antissimétrica: {A_oposta == A_transposta}")

B = sp.Matrix([[7, 9, 1],
                    [6, 3, 4],
                    [3, 3, 8]])
B_oposta = -B
B_transposta = B.transpose()

print(f"B é antissimétrica: {B_oposta == B_transposta}")
