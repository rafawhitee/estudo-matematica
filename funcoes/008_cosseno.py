import sympy as sp
import numpy as np
from plano_cartesiano.utils import PlanoCartesiano

# Inicializar símbolo
x = sp.symbols('x')

# função
funcao = sp.lambdify(x, sp.cos(x), 'numpy')

# Gerar valores de x
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 400)

plano_cartesiano = PlanoCartesiano()
plano_cartesiano.inserir_pontos(valores_eixo_x=x_vals, valores_eixo_y=funcao(x_vals), label=f'Função Cosseeno', cor="red")
plano_cartesiano.alterar_limites_eixos(limite_eixo_y=[-10, 10])
plano_cartesiano.renderizar()