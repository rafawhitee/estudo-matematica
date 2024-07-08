import sympy as sp

matriz = sp.Matrix([[3, 1, 2],
                    [1, 4, 3],
                    [2, 3, 5]])
matriz_transposta = matriz.transpose()

print(f"Matriz 1 é simétrica: {matriz == matriz_transposta}")

matriz_2 = sp.Matrix([[7, 9, 1],
                    [6, 3, 4],
                    [3, 3, 8]])
matriz_2_transposta = matriz_2.transpose()

print(f"Matriz 2 é simétrica: {matriz_2 == matriz_2_transposta}")
