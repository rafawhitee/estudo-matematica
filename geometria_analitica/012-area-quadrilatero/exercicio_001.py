import sympy as sp

# Calcular a área do quadrilátero de vértices A(1,5), B(6,5), C(6,1) e D(1,1)
A = (1,5)
B = (6,5)
C = (6,1)
D = (1,1)

matriz_1 = sp.Matrix([[A[0], A[1], 1],
                    [B[0], B[1], 1],
                    [C[0], C[1], 1]])
det_1 = matriz_1.det()

matriz_2 = sp.Matrix([[A[0], A[1], 1],
                    [C[0], C[1], 1],
                    [D[0], D[1], 1]])
det_2 = matriz_2.det()

area_quadrilatero = (sp.Abs(det_1) + sp.Abs(det_2)) / 2
print(f"Área do quadrilátero cujo vértices são {A}, {B}, {C} e {D}: {area_quadrilatero}")