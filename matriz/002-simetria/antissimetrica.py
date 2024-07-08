import sympy as sp

matriz = sp.Matrix([[0, 3],
                    [-3, 0]])
matriz_oposta = -matriz
matriz_transposta = matriz.transpose()

print(f"Matriz 1 é antissimétrica: {matriz_oposta == matriz_transposta}")

matriz_2 = sp.Matrix([[7, 9, 1],
                    [6, 3, 4],
                    [3, 3, 8]])
matriz_2_oposta = -matriz_2
matriz_2_transposta = matriz_2.transpose()

print(f"Matriz 2 é antissimétrica: {matriz_2_oposta == matriz_2_transposta}")
