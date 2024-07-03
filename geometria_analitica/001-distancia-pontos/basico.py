import numpy as np
import matplotlib.pyplot as plt
from utils import *

# Coordenadas 
A = (3,8)
B = (6,8)
C = (3,15)
D = (10,19)

distancia_ab = distancia_euclidiana(A, B)
distancia_ac = distancia_euclidiana(A, C)
distancia_ad = distancia_euclidiana(A, D)
distancia_bc = distancia_euclidiana(B, C)
distancia_bd = distancia_euclidiana(B, D)
distancia_cd = distancia_euclidiana(C, D)

# Substituindo os valores das coordenadas
print(f"Distância AB: {distancia_ab}\n")

print(f"Distância AC: {distancia_ac}\n")

print(f"Distância AD: {distancia_ad}\n")

print(f"Distância BC: {distancia_bc}\n")

print(f"Distância BD: {distancia_bd}\n")

print(f"Distância CD: {distancia_cd}\n")

# Cria vários valores
x_vals = np.linspace(0, 10, 400)

# Criar a figura e os eixos
fig, ax = plt.subplots()

# Coloca os Pontos 
ax.scatter(A[0], A[1], color='red', s=100) 
ax.annotate(f'A', xy=(A[0], A[1]), xytext=(A[0] - 20, A[1]), textcoords='offset points', arrowprops=dict(facecolor='red', arrowstyle='->'), ha='center')

ax.scatter(B[0], B[1], color='green', s=100) 
ax.annotate(f'B', xy=(B[0], B[1]), xytext=(B[0] + 20, B[1]), textcoords='offset points', arrowprops=dict(facecolor='green', arrowstyle='->'), ha='center')

ax.scatter(C[0], C[1], color='blue', s=100) 
ax.annotate(f'C', xy=(C[0], C[1]), xytext=(C[0] - 20, C[1]), textcoords='offset points', arrowprops=dict(facecolor='blue', arrowstyle='->'), ha='center')

ax.scatter(D[0], D[1], color='yellow', s=100) 
ax.annotate(f'D', xy=(D[0], D[1]), xytext=(D[0] - 20, D[1]), textcoords='offset points', arrowprops=dict(facecolor='yellow', arrowstyle='->'), ha='center')

# Coloca as distâncias entre os pontos (A e B)

# Entre A e B
x_vals_ab = np.linspace(min(A[0], B[0]), max(A[0], B[0]), 400)
equacao_reduzida_func_ab = equacao_reduzida_lambdify(A, B)
y_vals_ab = np.full_like(x_vals_ab, equacao_reduzida_func_ab(x_vals_ab))

ax.plot(x_vals_ab, y_vals_ab, label=f"Distância AB")
ax.set_title(distancia_ab)

# Entre A e C
y_vals_ac = np.linspace(min(A[1], C[1]), max(A[1], C[1]), 400)
equacao_reduzida_func_ac = equacao_reduzida_invertida_lambdify(A, C)
x_vals_ac = np.full_like(y_vals_ac, equacao_reduzida_func_ac(y_vals_ac))

ax.plot(x_vals_ac, y_vals_ac, label=f"Distância AC")
ax.set_title(distancia_ac)

# Entre A e D
x_vals_ad = np.linspace(min(A[0], D[0]), max(A[0], D[0]), 400)
equacao_reduzida_func_ad = equacao_reduzida_lambdify(A, D)
ax.plot(x_vals_ad, equacao_reduzida_func_ad(x_vals_ad), label=f"Distância AD")
ax.set_title(distancia_ad)

# Entre B e C
x_vals_bc = np.linspace(min(B[0], C[0]), max(B[0], C[0]), 400)
equacao_reduzida_func_bc = equacao_reduzida_lambdify(B, C)
print(f"{equacao_reduzida(B, C)}")
ax.plot(x_vals_bc, equacao_reduzida_func_bc(x_vals_bc), label=f"Distância BC")
ax.set_title(distancia_bc)

# Entre B e D
x_vals_bd = np.linspace(min(B[0], D[0]), max(B[0], D[0]), 400)
equacao_reduzida_func_bd = equacao_reduzida_lambdify(B, D)
ax.plot(x_vals_bd, equacao_reduzida_func_bd(x_vals_bd), label=f"Distância BD")
ax.set_title(distancia_bd)

# Entre C e D
x_vals_cd = np.linspace(min(C[0], D[0]), max(C[0], D[0]), 400)
equacao_reduzida_func_cd = equacao_reduzida_lambdify(C, D)
ax.plot(x_vals_cd, equacao_reduzida_func_cd(x_vals_cd), label=f"Distância CD")
ax.set_title(distancia_cd)

# Configurar o plano cartesiano
ax.legend()
ax.grid(True)

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