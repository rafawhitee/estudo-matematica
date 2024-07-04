import sympy as sp
from utils import *

x, y = sp.symbols("x y")

reta_1 = 2*x + 5
reta_2 = -3*x - 1
reta_3 = 0*x + 3
reta_4 = -x + 2

print(f"ângulo agudo entre a reta 1 e 2: {angulo_agudo(reta_1, reta_2)}")
print(f"ângulo agudo entre a reta 3 e 4: {angulo_agudo(reta_3, reta_4)}")