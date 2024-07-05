import sympy as sp
from utils import *

# Ponto (3,2)
P = (3,2)

# Equação da Circunferência --> (x-2)² + (y+1)² = 9
x, y = sp.symbols("x y")
equacao_circunferencia = sp.Eq(9, (x - 2)**2 + (y + 1)**2)
raio = 3 # Raio é 3 (pois na equação está = 9)
C = (2, -1) # 2 é o x0 e y0 é -1

distancia_ponto_centro_circunferencia = distancia_euclidiana(P, C)
if distancia_ponto_centro_circunferencia > raio:
    print("Ponto está fora da circunferência")
elif distancia_ponto_centro_circunferencia == raio:
    print("Ponto está em cima da circunferência")
else:
    print("Ponto está dentro da circunferência")