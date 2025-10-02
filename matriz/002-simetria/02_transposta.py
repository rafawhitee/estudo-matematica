import sympy as sp

A = sp.Matrix([[1, 2, 3],
                [4, 5, 6]])
print(f"Matriz: {A}")

# A transposta inverte linha e coluna
# O que era Linha, vira coluna, e o que era coluna, se torna linha
# Então, se a Matriz acima tinha 2 linhas e 3 colunas (Matriz 2x3), sua transposta vai ser uma Matriz 3x2 (3 linhas e 2 colunas)
print(f"Matriz Transposta: {A.transpose()}")
