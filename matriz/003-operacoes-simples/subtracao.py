import sympy as sp

A = sp.Matrix([[5, 2],
                [-7, 9]])

B = sp.Matrix([[3, 6],
                [-1, 4]])

C = sp.Matrix([[5, 1, 2],
                [8, 2, -3]])

print(f"Subtração de A com B: {A - B}")
print(f"Subtração de B com A: {B - A}")

try:
    print(f"Soma de A com C: {A - C}")
except:
    print(f"A e C possui dimensões diferentes, portanto não é possível efetuar a operação de subtração")