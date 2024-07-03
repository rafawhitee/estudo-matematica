import numpy as np

# Cria os 3 pontos
A = (2, 5)
B = (3, 9)
C = (4, 11)

# Criar a matriz 3x3
M = np.array([
    [A[0], A[1], 1],
    [B[0], B[1], 1],
    [C[0], C[1], 1]
])

# calcula o determinante da matriz
det = np.linalg.det(M)
print(f"Determinante: {det}")
print(f"São Colineares (alinhados): {det == 0}")