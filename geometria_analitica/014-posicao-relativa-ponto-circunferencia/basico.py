import numpy as np
from utils import *
from plano_cartesiano.utils import PlanoCartesiano

# Ponto Qualquer (3,2)
P = (3,2)

# Equação da Circunferência --> (x-2)² + (y+1)² = 9
C = (2, -1) # Coordenadas do Centro da Circunferência, 2 é o x0 e y0 é -1
raio = 3 # Raio é 3 (pois na equação está = 9)

distancia_ponto_centro_circunferencia = distancia_euclidiana(P, C)
if distancia_ponto_centro_circunferencia > raio:
    print("Ponto está fora da circunferência")
elif distancia_ponto_centro_circunferencia == raio:
    print("Ponto está em cima da circunferência")
else:
    print("Ponto está dentro da circunferência")

# cria os pontos da circunferência
theta = np.linspace(0, 2 * np.pi, 100)
x = C[0] + raio * np.cos(theta)
y = C[1] + raio * np.sin(theta)

# Criar a figura e os eixos
plano_cartesiano = PlanoCartesiano()

# Insere os pontos da circunferência
plano_cartesiano.inserir_pontos(valores_eixo_x=x, valores_eixo_y=y)

# Coloca os Pontos e suas Anotações
plano_cartesiano.inserir_ponto(P, cor='red', tamanho=100)
plano_cartesiano.inserir_anotacao(coordenada=P, titulo="Ponto Qualquer")

plano_cartesiano.inserir_ponto(C, cor='blue', tamanho=100)
plano_cartesiano.inserir_anotacao(coordenada=C, titulo="Centro")

plano_cartesiano.alterar_limites_eixos([-5, 7], [-5, 7])
plano_cartesiano.renderizar()