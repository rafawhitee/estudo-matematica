import sympy as sp
from utils import *

# Quais são os possíveis valores de c para que os pontos (c , 3), (2 , c) e (14, -3) sejam colineares?

# Cria os 3 pontos
c = sp.symbols("c")

A = (c,3)
B = (2,c)
C = (14,-3)

# calcula o coeficiente angular entre A e C (como tem um símbolo, ele retornará uma equação)
coeficiente_angular_ac = coeficiente_angular(A, C)
print(f"Coeficiente AC: {coeficiente_angular_ac}")

# calcula o coeficiente angular entre B e C (como tem um símbolo, ele retornará uma equação)
coeficiente_angular_bc = coeficiente_angular(B, C)
print(f"Coeficiente BC: {coeficiente_angular_bc}")

# cria a equação igualando ambos coeficiente angulares acimas, pois para ser colinear, eles devem ser iguais
equation = sp.Eq(coeficiente_angular_ac, coeficiente_angular_bc)
print(f"Equação --> {equation}")

# manda solucionar a equação
solutions = sp.solve(equation)

print(f"Solução --> {solutions} \n")

for solution in solutions:
    # Provas reais:
    A = (solution,3)
    B = (2,solution)
    C = (14,-3)

    coeficiente_angular_ac = coeficiente_angular(A, C)
    print(f"Coeficiente AC: {coeficiente_angular_ac}")

    coeficiente_angular_bc = coeficiente_angular(B, C)
    print(f"Coeficiente BC: {coeficiente_angular_bc}")

    colineares = coeficiente_angular_ac == coeficiente_angular_bc
    print(f"São Colineares: {colineares} \n")