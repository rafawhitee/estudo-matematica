import numpy as np
import sympy as sp
from plano_cartesiano.utils import PlanoCartesiano

# declara o símbolo X
x = sp.symbols('x')

# cria como expressão
expressao = x**3 + 2*x**2 - 20

# função
funcao = sp.lambdify(x, expressao, 'numpy')

# valores de X
x_vals = np.linspace(-10, 10, 400)

# mostra um exemplo com X = 2
print(f"Resultado de 'x³ + 2x² - 20' com x = 2: {funcao(2)}") 

# a partir dos valores de X, joga na expressão para retornar o Y para poder mostrar o gráfico
y_vals = funcao(x_vals)

plano_cartesiano = PlanoCartesiano()
plano_cartesiano.inserir_pontos(valores_eixo_x=x_vals, valores_eixo_y=y_vals, label=f'{expressao}', cor="red")
plano_cartesiano.alterar_limites_eixos([min(x_vals) - 2, max(x_vals) + 2], [min(y_vals) - 200, max(y_vals) + 200])
plano_cartesiano.renderizar()