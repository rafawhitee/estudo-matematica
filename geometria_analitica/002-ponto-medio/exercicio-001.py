import sympy as sp
from utils import *

# Determine o valor de x para que o ponto M(2 , 3) seja o ponto médio do segmento de extremos A(x , 5) e B(3 , x).

x = sp.symbols("x")

A = (x,5)
B = (3,x)
M = (2,3)

ponto_medio_x = sp.Eq((A[0] + B[0]) / 2, M[0])
print(f"Equação do Ponto Médio X: {ponto_medio_x}")
print(f"Resolução do Ponto Médio X: {sp.solve(ponto_medio_x)}")

ponto_medio_y = sp.Eq((A[1] + B[1]) / 2, M[1])
print(f"Equação do Ponto Médio Y: {ponto_medio_y}")
print(f"Resolução do Ponto Médio Y: {sp.solve(ponto_medio_y)}")
