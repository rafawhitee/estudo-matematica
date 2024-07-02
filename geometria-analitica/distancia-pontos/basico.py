import matplotlib.pyplot as plt
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

# Criar a figura e os eixos
fig, ax = plt.subplots()

ax.scatter(A[0], A[1], color='red', s=100) 
ax.scatter(B[0], B[1], color='green', s=100) 
ax.scatter(C[0], C[1], color='blue', s=100) 
ax.scatter(D[0], D[1], color='yellow', s=100) 

# Configurar o plano cartesiano
ax.axhline(y=0, color='k')  # Eixo x
ax.axvline(x=0, color='k')  # Eixo y
ax.grid(True, which='both')

# Adicionar título e legendas
plt.title('Distância entre os Pontos')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

# Definir os limites dos eixos
ax.set_xlim([-10, 25])
ax.set_ylim([-10, 25])

plt.show()