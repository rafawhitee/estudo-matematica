import sympy as sp
from utils import *

x, y = sp.symbols("x y")

P = (2,3)
reta_1 = 3*x - 4*y + 1
reta_2 = 6*x + 2*y + 5

print(f"Distância entre a Reta 1 e o Ponto {P}: {distancia_reta_ponto(reta_1, P)}")
print(f"Distância entre a Reta 2 e o Ponto {P}: {distancia_reta_ponto(reta_2, P)}")