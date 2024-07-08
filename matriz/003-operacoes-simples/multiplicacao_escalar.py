import sympy as sp

A = sp.Matrix([[5, 2],
                [-7, 9]])

B = sp.Matrix([[3, 6],
                [-1, 4]])

C = sp.Matrix([[5, 1, 2],
                [8, 2, -3]])

print(f"Matriz A multiplicada por 3: {A * 3}")
print(f"Matriz B multiplicada por 4: {B * 4}")
print(f"Matriz B multiplicada por -2: {C * -2}")
