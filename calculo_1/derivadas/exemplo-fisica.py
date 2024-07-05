import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

from plano_cartesiano.utils import PlanoCartesiano

# Definir a variável simbólica
t = sp.symbols('t')

# Definir a função de posição (5t² + 3t + 2)
position_expression = 5 * t**2 + 3 * t + 2

# Calcular a derivada da posição (velocidade)
velocity_expression = sp.diff(position_expression, t)

# Calcular a derivada da velocidade (aceleração)
acceleration_expression = sp.diff(velocity_expression, t)

# Converter as funções simbólicas para funções numéricas
position_function = sp.lambdify(t, position_expression, 'numpy')
velocity_function = sp.lambdify(t, velocity_expression, 'numpy')
acceleration_function = sp.lambdify(t, acceleration_expression, 'numpy')

# Valores de tempo para o gráfico
t_vals = np.linspace(0, 10, 400)
s_vals = position_function(t_vals)
v_vals = velocity_function(t_vals)
a_vals = np.full_like(t_vals, acceleration_function(t_vals))

# monta o plano cartesiano para renderizar
plano_cartesiano = PlanoCartesiano(linhas=3, figsize=(8,12))
plano_cartesiano.inserir_pontos(valores_eixo_x=t_vals, valores_eixo_y=s_vals, titulo='Posição', label='s(t) = 5t² + 3t + 2', cor="green", index=0)
plano_cartesiano.inserir_pontos(valores_eixo_x=t_vals, valores_eixo_y=v_vals, titulo='Velocidade', label='v(t) = ds/dt = 10t + 3', cor="orange", index=1)
plano_cartesiano.inserir_pontos(valores_eixo_x=t_vals, valores_eixo_y=a_vals, titulo='Aceleração', label='a(t) = dv/dt = 10',  cor="red", index=2)
plano_cartesiano.renderizar(tight=True)