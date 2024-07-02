import matplotlib.pyplot as plt
from geometria_analitica.utils import distancia_euclidiana

# Coordenadas 
A = (3,8)
B = (6,8)
C = (3,12)
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