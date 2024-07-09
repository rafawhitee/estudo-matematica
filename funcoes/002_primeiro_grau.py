from matplotlib.animation import FuncAnimation
import numpy as np
import sympy as sp
from plano_cartesiano.utils import PlanoCartesiano

# declara o símbolo X
x = sp.symbols('x')

# cria uma função python que retorna a expressão da função de primeiro grau
def expressao(coeficiente_angular, coeficiente_linear):
    return coeficiente_angular*x + coeficiente_linear

# cria valores para X
x_vals = np.linspace(-10, 10, 400)

plano_cartesiano = PlanoCartesiano()

min_arange = 1
max_arange = 100

def funcao_animacao_somando_coeficiente_angular(i):
    plano_cartesiano.get_ax().clear()
    express = expressao(i, 2)
    funcao = sp.lambdify(x, express, 'numpy')
    y_vals = np.full_like(x_vals, funcao(x_vals))
    plano_cartesiano.inserir_pontos(valores_eixo_x=x_vals, valores_eixo_y=y_vals, label=f"{express}")
    plano_cartesiano.alterar_limites_eixos([-20, 20], [-20, max_arange + (max_arange * 0.5)])
    plano_cartesiano.configurar_eixos()

def funcao_animacao_somando_coeficiente_linear(i):
    plano_cartesiano.get_ax().clear()
    express = expressao(2, i)
    funcao = sp.lambdify(x, express, 'numpy')
    y_vals = np.full_like(x_vals, funcao(x_vals))
    plano_cartesiano.inserir_pontos(valores_eixo_x=x_vals, valores_eixo_y=y_vals, label=f"{express}")
    plano_cartesiano.alterar_limites_eixos([-20, 20], [-20, max_arange + (max_arange * 0.5)])
    plano_cartesiano.configurar_eixos()

animacao = FuncAnimation(plano_cartesiano.get_fig(), funcao_animacao_somando_coeficiente_angular, frames=np.arange(min_arange, max_arange), interval=1)

plano_cartesiano.renderizar()