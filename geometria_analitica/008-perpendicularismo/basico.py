import sympy as sp
from utils import *

x, y = sp.symbols("x y")

reta_1 = 2*x - 3
reta_2 = 4*x + 5
reta_3 = -1/2*x - 2
reta_4 = 7*x - 5

print(f"Reta 1 e 2 são perpendiculares: {perpendiculares(reta_1, reta_2)}")
print(f"Reta 1 e 3 são perpendiculares: {perpendiculares(reta_1, reta_3)}")
print(f"Reta 1 e 4 são perpendiculares: {perpendiculares(reta_1, reta_4)}")
print(f"Reta 2 e 3 são perpendiculares: {perpendiculares(reta_2, reta_3)}")
print(f"Reta 2 e 4 são perpendiculares: {perpendiculares(reta_2, reta_4)}")
print(f"Reta 3 e 4 são perpendiculares: {perpendiculares(reta_3, reta_4)}")
print(f"Coeficiente Angular para a reta ser perpendicular da Reta 4: {coeficiente_angular_para_ser_perpendicular(reta_4)}")