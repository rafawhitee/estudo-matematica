import sympy as sp

# Cria os 4 pontos que formam o quadrilátero
A = (1,8)
B = (4,7)
C = (3,5)
D = (6,9)

# para calcular, basta dividir o quadrilátero em 2 triângulos, traçando uma linha horizontal, então irá fazer uma combinação de 2 determinantes

# Cria a matriz 3x3 (primeiro triângulo que pega os vértices A, B e C)
matriz_1 = sp.Matrix([[A[0], A[1], 1],
                    [B[0], B[1], 1],
                    [C[0], C[1], 1]])

det_1 = matriz_1.det()

# Cria a segunda matriz 3x3 (segundo triângulo que pega os vértices A, C, D)
matriz_2 = sp.Matrix([[A[0], A[1], 1],
                    [C[0], C[1], 1],
                    [D[0], D[1], 1]])

det_2 = matriz_2.det()

area_quadrilatero = (sp.Abs(det_1) + sp.Abs(det_2)) / 2
print(f"Área do quadrilátero cujo vértices são {A}, {B}, {C} e {D}: {area_quadrilatero}")