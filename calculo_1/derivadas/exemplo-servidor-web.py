import numpy as np
from sympy import symbols, diff, lambdify

from plano_cartesiano.utils import PlanoCartesiano

# Constantes
A = 100
B = 0.5

n = symbols('n')
expression = 100/n - 1/2*n

derivative = diff(expression, n)

# Converter as expressões simbólicas para funções numéricas
expression_func = lambdify(n, expression, 'numpy')
derivative_func = lambdify(n, derivative, 'numpy')

# gera um vetor de valores para o N
N_vals = np.linspace(1, 20, 400)

# a partir do vetor de valores de N, gera o resultado da função
T_vals = expression_func(N_vals)
T_prime_vals = derivative_func(N_vals)

# Calcular o ponto crítico
N_critical = np.sqrt(A / B)
T_critical = expression_func(N_critical)

# monta o plano cartesiano para renderizar
plano_cartesiano = PlanoCartesiano()
plano_cartesiano.alterar_limites_eixos(limite_eixo_x=[0,20], limite_eixo_y=[-20, max(T_vals) + 20])
plano_cartesiano.inserir_pontos(valores_eixo_x=N_vals, valores_eixo_y=T_vals, label='Tempo de Resposta T(N)')
plano_cartesiano.inserir_ponto(coordenada=(N_critical, T_critical))
plano_cartesiano.inserir_anotacao(coordenada=(N_critical, T_critical), titulo=f'Número Ótimo de Servidores: {N_critical:.2f}', coordenada_titulo=(N_critical, T_critical + 10))
plano_cartesiano.renderizar()