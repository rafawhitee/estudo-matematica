import numpy as np
import matplotlib.pyplot as plt
from utils import *

A = (3,8)
B = (12,8)
C = (3,20)

ponto_baricentro = baricentro(A, B, C)
print(f"Baricentro do Triângulo ABC: {ponto_baricentro}")

# Criar a figura e os eixos
fig, ax = plt.subplots()

# Coloca os Pontos 
ax.scatter(A[0], A[1], color='red', s=100) 
ax.annotate(f'A', xy=(A[0], A[1]), xytext=(A[0] - 25, A[1]), textcoords='offset points', arrowprops=dict(facecolor='red', arrowstyle='->'), ha='center')

ax.scatter(B[0], B[1], color='black', s=100) 
ax.annotate(f'B', xy=(B[0], B[1]), xytext=(B[0] + 20, B[1]), textcoords='offset points', arrowprops=dict(facecolor='red', arrowstyle='->'), ha='center')

ax.scatter(C[0], C[1], color='blue', s=100) 
ax.annotate(f'C', xy=(C[0], C[1]), xytext=(C[0] - 25, C[1]), textcoords='offset points', arrowprops=dict(facecolor='red', arrowstyle='->'), ha='center')

ax.scatter(ponto_baricentro[0], ponto_baricentro[1], color='orange', s=100) 
ax.annotate(f'Centro', xy=(ponto_baricentro[0], ponto_baricentro[1]), xytext=(ponto_baricentro[0], ponto_baricentro[1] + 5), textcoords='offset points', arrowprops=dict(facecolor='pink', arrowstyle='->'), ha='center')

# Coloca as distâncias entre os pontos para formar o triângulo
x_vals_ab = np.linspace(min(A[0], B[0]), max(A[0], B[0]), 400)
equacao_reduzida_func_ab = equacao_reduzida_lambdify(A, B)
y_vals_ab = np.full_like(x_vals_ab, equacao_reduzida_func_ab(x_vals_ab))
ax.plot(x_vals_ab, y_vals_ab, label=f"Distância AB")

y_vals_ac = np.linspace(min(A[1], C[1]), max(A[1], C[1]), 400)
equacao_reduzida_func_ac = equacao_reduzida_invertida_lambdify(A, C)
x_vals_ac = np.full_like(y_vals_ac, equacao_reduzida_func_ac(y_vals_ac))
ax.plot(x_vals_ac, y_vals_ac, label=f"Distância AC")

x_vals_bc = np.linspace(min(B[0], C[0]), max(B[0], C[0]), 400)
equacao_reduzida_func_bc = equacao_reduzida_lambdify(B, C)
ax.plot(x_vals_bc, equacao_reduzida_func_bc(x_vals_bc), label=f"Distância BC")

# Configurar o plano cartesiano
ax.legend()
ax.grid(True)

ax.axhline(y=0, color='k')  # Eixo x
ax.axvline(x=0, color='k')  # Eixo y
ax.grid(True, which='both')

# Adicionar título e legendas
plt.title('Baricentro do Triângulo')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

# Definir os limites dos eixos
ax.set_xlim([-10, 25])
ax.set_ylim([-10, 25])

plt.show()