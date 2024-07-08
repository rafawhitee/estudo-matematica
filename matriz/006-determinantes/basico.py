import sympy as sp

# matriz de ordem 1
A = sp.Matrix([[1]])
print(f"Determinante de matriz de ordem 1: {A.det()}")

# matriz de ordem 2
B = sp.Matrix([[1, 4], 
               [3, 6]])
print(f"Determinante de matriz de ordem 2: {B.det()}")

# matriz de ordem 3
C = sp.Matrix([[3, 5, 8], 
               [-2, 3, 9],
               [-5, 0, 2]])
print(f"Determinante de matriz de ordem 3: {C.det()}")

# matriz de ordem 4 (a regra da ordem 4 serve para todos em diante)
D = sp.Matrix([[1, -3, 4, 6], 
               [-3, 0, 2, 1],
               [2, 3, 5, -2],
               [1, 5, 6, -8]])
print(f"Determinante de matriz de ordem 4: {D.det()}")