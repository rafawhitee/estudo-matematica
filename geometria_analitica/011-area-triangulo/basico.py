import sympy as sp

# Cria os 3 pontos que formam o triângulo
A = (2,5)
B = (3,9)
C = (4,1)

# Cria a matriz 3x3
matriz = sp.Matrix([[A[0], A[1], 1],
                   [B[0], B[1], 1],
                   [C[0], C[1], 1]])

# calcula o determinante da matriz
det = matriz.det()
area_triangulo = sp.Abs(det) / 2
print(f"Área do triângulo cujo vértices são {A}, {B} e {C}: {area_triangulo}")