import sympy as sp

# matriz 2x3
A = sp.Matrix([[2, 3, 1],
                [0, 1, 2]])

# matriz 3x2
B = sp.Matrix([[2, 0],
                [1, -1],
                [3, 5]])

# matriz 2x2
C = sp.Matrix([[2, 0],
                [1, -1]])

# como o número de colunas da primeira (3) é igual ao número de linhas da segunda (3), pode efetuar a multiplicação
print(f"Multiplicação entre A e B: {A * B}")

# Entre A e C vai dar erro, pois a Regra principal está incorreta
# o número de colunas da primeira é diferente ao número de linhas da segunda
try:
    print(f"Multiplicação entre A e C: {A * C}")
except:
    print(f"O número de colunas da primeira matriz é diferente do número de linhas da segunda matriz, portanto não é possível efetuar a multiplicação")