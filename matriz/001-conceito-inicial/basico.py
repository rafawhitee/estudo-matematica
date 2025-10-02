import sympy as sp

# Podemos entender uma matriz como uma forma de representar um conjunto de valores em um formato parecido com uma tabela. Uma matriz A 
# é uma matriz que tem linhas e colunas.
 
# possui somente 1 linha e 1 coluna
matriz_unitaria = sp.Matrix([[1]])
print(f"Matriz Unitária: {matriz_unitaria}")

# possui somente 1 linha
matriz_linha = sp.Matrix([[1, 2, 3]])
print(f"Matriz Linha: {matriz_linha}")

# possui somente 1 coluna
matriz_coluna = sp.Matrix([[1],
                           [2],
                           [3]])
print(f"Matriz Coluna: {matriz_coluna}")

# número de colunas > número de linhas
matriz_retangular = sp.Matrix([[1, 2, 3],
                               [4, 5, 6]])
print(f"Matriz Retangular: {matriz_retangular}")

# número de linhas = número de colunas
matriz_quadrada = sp.Matrix([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]])
print(f"Matriz Quadrada: {matriz_quadrada}")