import numpy as np
import sympy as sp
from plano_cartesiano.utils import PlanoCartesiano

# símbolos
x = sp.symbols('x')

log_natural = sp.log(x) # logaritmo natural (neuperiana)
funcao_natural = sp.lambdify(x, log_natural, 'numpy')

log_base_binaria = sp.log(x, 2) # logaritmo na base 2 (binária)
funcao_base_binaria = sp.lambdify(x, log_base_binaria, 'numpy')

log_base_decimal = sp.log(x, 10) # logaritmo na base 10 (decimal)
funcao_base_decimal = sp.lambdify(x, log_base_decimal, 'numpy')

# valores de X
x_vals = np.linspace(-10, 10, 400)

plano_cartesiano = PlanoCartesiano()
plano_cartesiano.inserir_pontos(valores_eixo_x=x_vals, valores_eixo_y=funcao_natural(x_vals), label=f'Log na Base Neuperiana', cor="red")
plano_cartesiano.inserir_pontos(valores_eixo_x=x_vals, valores_eixo_y=funcao_base_binaria(x_vals), label=f'Log na Base Binária', cor="green")
plano_cartesiano.inserir_pontos(valores_eixo_x=x_vals, valores_eixo_y=funcao_base_decimal(x_vals), label=f'Log na Base Decimal', cor="blue")
plano_cartesiano.renderizar()