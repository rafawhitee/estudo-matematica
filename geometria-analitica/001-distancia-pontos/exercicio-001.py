import matplotlib.pyplot as plt
import sympy as sp

# Definindo as variáveis da fórmula
x1, y1 = sp.symbols('x1 y1')
x2, y2 = sp.symbols('x2 y2')

# Fórmula da distância euclidiana
distancia = sp.sqrt((x2 - x1)**2 + (y2 - y1)**2)

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

## Gráfico dos 3 pontos que formam o triângulo acima

# Criar a figura e os eixos
fig, ax = plt.subplots()

ax.scatter(T1[0], T1[1], color='red', s=100) 
ax.scatter(T2[0], T2[1], color='green', s=100) 
ax.scatter(T3[0], T3[1], color='blue', s=100) 

# Configurar o plano cartesiano
ax.axhline(y=0, color='k')  # Eixo x
ax.axvline(x=0, color='k')  # Eixo y
ax.grid(True, which='both')

# Adicionar título e legendas
plt.title('3 Pontos que formam o Triângulo do exercício')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

# Definir os limites dos eixos
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])

plt.show()
