import numpy as np
import sympy as sp
from plano_cartesiano.utils import PlanoCartesiano

# declara o símbolo X
x = sp.symbols('x')

# cria valores para X
x_vals = np.linspace(-10, 10, 400)

# cria como expressão
expressao = 4*x - 5

# transforma em função
funcao = sp.lambdify(x, expressao, 'numpy')

# mostra um exemplo com X = 2
print(f"Resultado de '4x - 5' com x = 2: {funcao(2)}") 

# a partir dos valores de X, joga na expressão para retornar o Y para poder mostrar o gráfico
y_vals = np.full_like(x_vals, funcao(x_vals))

plano_cartesiano = PlanoCartesiano()
plano_cartesiano.inserir_pontos(valores_eixo_x=x_vals, valores_eixo_y=y_vals, label=f'{expressao}', cor="red")
plano_cartesiano.alterar_limites_eixos([min(x_vals) - 5, max(x_vals) + 5], [min(y_vals) - 5, max(y_vals) + 5])
plano_cartesiano.renderizar()