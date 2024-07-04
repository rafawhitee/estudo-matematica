import sympy as sp
from utils import *

x, y = sp.symbols("x y")

reta_1 = 2*x - 5
reta_2 = 2*x + 12
reta_3 = 4*x - 2
reta_4 = 2*x - 5

print(f"Reta 1 e 2 são paralelas: {paralelas(reta_1, reta_2)} \n")
print(f"Reta 1 e 3 são paralelas: {paralelas(reta_1, reta_3)} \n")
print(f"Reta 1 e 4 são paralelas: {paralelas(reta_1, reta_4)} \n")

print(f"Reta 2 e 3 são paralelas: {paralelas(reta_2, reta_3)} \n")
print(f"Reta 2 e 4 são paralelas: {paralelas(reta_2, reta_4)} \n")

print(f"Reta 3 e 4 são paralelas: {paralelas(reta_3, reta_4)} \n")

print(f"Reta 1 e 2 são paralelas coincidentes: {coincidentes(reta_1, reta_2)} \n")
print(f"Reta 1 e 3 são paralelas coincidentes: {coincidentes(reta_1, reta_3)} \n")
print(f"Reta 1 e 4 são paralelas coincidentes: {coincidentes(reta_1, reta_4)} \n")

print(f"Reta 2 e 3 são paralelas coincidentes: {coincidentes(reta_2, reta_3)} \n")
print(f"Reta 2 e 4 são paralelas coincidentes: {coincidentes(reta_2, reta_4)} \n")

print(f"Reta 3 e 4 são paralelas coincidentes: {coincidentes(reta_3, reta_4)} \n")