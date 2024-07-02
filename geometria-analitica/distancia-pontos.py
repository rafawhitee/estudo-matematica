import sympy as sp

# Definindo as variáveis da fórmula
x1, y1 = sp.symbols('x1 y1')
x2, y2 = sp.symbols('x2 y2')

# Fórmula da distância euclidiana
distancia = sp.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Coordenadas 
A = (3,8)
B = (6,8)
C = (3,12)
D = (10,19)

# Substituindo os valores das coordenadas
print(f"Distância AB: {distancia.subs({x1: A[0], y1: A[1], x2: B[0], y2: B[1]}).evalf()}\n")

print(f"Distância AC: {distancia.subs({x1: A[0], y1: A[1], x2: C[0], y2: C[1]}).evalf()}\n")

print(f"Distância AD: {distancia.subs({x1: A[0], y1: A[1], x2: D[0], y2: D[1]}).evalf()}\n")

print(f"Distância BC: {distancia.subs({x1: B[0], y1: B[1], x2: C[0], y2: C[1]}).evalf()}\n")

print(f"Distância BD: {distancia.subs({x1: B[0], y1: B[1], x2: D[0], y2: D[1]}).evalf()}\n")

print(f"Distância CD: {distancia.subs({x1: C[0], y1: C[1], x2: D[0], y2: D[1]}).evalf()}\n")

# Exemplo EEAR:
# O triângulo de vértices A(7,3), B(-4,3) e C(-4,-2) e:
#   a) Escaleno
#   b) Isósceles
#   c) Equiângulo
#   d) Obstusângulo

T1 = (7,3)
T2 = (-4,3)
T3 = (-4,-2)

print(f"Distância T1 para T2: {distancia.subs({x1: T1[0], y1: T1[1], x2: T2[0], y2: T2[1]}).evalf()}")
print(f"Distância T1 para T3: {distancia.subs({x1: T1[0], y1: T1[1], x2: T3[0], y2: T3[1]}).evalf()}")
print(f"Distância T2 para T3: {distancia.subs({x1: T2[0], y1: T2[1], x2: T3[0], y2: T3[1]}).evalf()}")

# os lados são diferentes, logo é a Letra A (Escaleno)