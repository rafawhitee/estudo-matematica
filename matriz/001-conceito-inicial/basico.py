import sympy as sp

matriz_unitaria = sp.Matrix([[1]])
print(f"Matriz Unitária: {matriz_unitaria}")

matriz_linha = sp.Matrix([[1, 2, 3]])
print(f"Matriz Linha: {matriz_linha}")

matriz_coluna = sp.Matrix([[1],
                           [2],
                           [3]])
print(f"Matriz Coluna: {matriz_coluna}")

matriz_retangular = sp.Matrix([[1, 2, 3],
                               [4, 5, 6]])
print(f"Matriz Retangular: {matriz_retangular}")

matriz_quadrada = sp.Matrix([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]])
print(f"Matriz Quadrada: {matriz_quadrada}")