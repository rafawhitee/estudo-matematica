import matplotlib.pyplot as plt
from utils import distancia_euclidiana

# Demonstre que o triãngulo de vérticas A(8,2), B(3,7) e C(2,1) é isósceles. E em seguida, calcule seu perímetro.

T1 = (8,2)
T2 = (3,7)
T3 = (2,1)

distancia_t1_t2 = distancia_euclidiana(T1, T2)
distancia_t1_t3 = distancia_euclidiana(T2, T3)
distancia_t2_t3 = distancia_euclidiana(T2, T3)

print(f"Distância T1 para T2: {distancia_t1_t2}")
print(f"Distância T1 para T3: {distancia_t1_t3}")
print(f"Distância T2 para T3: {distancia_t2_t3}")
print(f"Perímetro: {distancia_t1_t2 + distancia_t1_t3 + distancia_t2_t3}")

# a distãncia T1 para T3 é igual a distãncia de T2 para T3, e T1 é diferente para T2, logo, somente 2 lados são iguais, confirmando que é isósceles.
# o perímetro é só somar

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
