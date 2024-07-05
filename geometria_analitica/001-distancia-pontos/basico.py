import numpy as np
import matplotlib.pyplot as plt
from utils import *
from plano_cartesiano.utils import PlanoCartesiano

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
plano_cartesiano = PlanoCartesiano()

# Coloca os Pontos 
plano_cartesiano.inserir_ponto(A, cor='red', tamanho=100)
plano_cartesiano.inserir_ponto(B, cor='green', tamanho=100)
plano_cartesiano.inserir_ponto(C, cor='blue', tamanho=100)
plano_cartesiano.inserir_ponto(D, cor='yellow', tamanho=100)

# Coloca as distâncias entre os pontos

# Entre A e B
x_vals_ab = np.linspace(min(A[0], B[0]), max(A[0], B[0]), 400)
equacao_reduzida_func_ab = equacao_reduzida_lambdify(A, B)
y_vals_ab = np.full_like(x_vals_ab, equacao_reduzida_func_ab(x_vals_ab))
plano_cartesiano.inserir_pontos(valores_eixo_x=x_vals_ab, valores_eixo_y=y_vals_ab, label="Distância AB")

# Entre A e C
y_vals_ac = np.linspace(min(A[1], C[1]), max(A[1], C[1]), 400)
equacao_reduzida_func_ac = equacao_reduzida_invertida_lambdify(A, C)
x_vals_ac = np.full_like(y_vals_ac, equacao_reduzida_func_ac(y_vals_ac))
plano_cartesiano.inserir_pontos(valores_eixo_x=np.full_like(y_vals_ac, equacao_reduzida_func_ac(y_vals_ac)), valores_eixo_y=y_vals_ac, label="Distância AC")

# Entre A e D
x_vals_ad = np.linspace(min(A[0], D[0]), max(A[0], D[0]), 400)
equacao_reduzida_func_ad = equacao_reduzida_lambdify(A, D)
y_vals_ad = equacao_reduzida_func_ad(x_vals_ad)
plano_cartesiano.inserir_pontos(valores_eixo_x=x_vals_ad, valores_eixo_y=y_vals_ad, label="Distância AD")

# Entre B e C
x_vals_bc = np.linspace(min(B[0], C[0]), max(B[0], C[0]), 400)
equacao_reduzida_func_bc = equacao_reduzida_lambdify(B, C)
y_vals_bc = equacao_reduzida_func_bc(x_vals_bc)
plano_cartesiano.inserir_pontos(valores_eixo_x=x_vals_bc, valores_eixo_y=y_vals_bc, label="Distância AD")

# Entre B e D
x_vals_bd = np.linspace(min(B[0], D[0]), max(B[0], D[0]), 400)
equacao_reduzida_func_bd = equacao_reduzida_lambdify(B, D)
y_vals_bd = equacao_reduzida_func_bd(x_vals_bd)
plano_cartesiano.inserir_pontos(valores_eixo_x=x_vals_bd, valores_eixo_y=y_vals_bd, label="Distância BD")

# Entre C e D
x_vals_cd = np.linspace(min(C[0], D[0]), max(C[0], D[0]), 400)
equacao_reduzida_func_cd = equacao_reduzida_lambdify(C, D)
y_vals_cd = equacao_reduzida_func_cd(x_vals_cd)
plano_cartesiano.inserir_pontos(valores_eixo_x=x_vals_cd, valores_eixo_y=y_vals_cd, label="Distância CD")

plano_cartesiano.alterar_limites_eixos([-10, 25], [-10, 25])
plano_cartesiano.renderizar()