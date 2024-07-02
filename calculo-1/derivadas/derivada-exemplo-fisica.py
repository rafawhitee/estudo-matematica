import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

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

# Criar a figura e os eixos
fig, ax = plt.subplots(3, 1, figsize=(8, 12))

# Plotar a função de posição
ax[0].plot(t_vals, s_vals, label='s(t) = 5t² + 3t + 2')
ax[0].set_title('Posição')
ax[0].set_xlabel('Tempo (s)')
ax[0].set_ylabel('Posição (m)')
ax[0].legend()
ax[0].grid(True)

# Plotar a função de velocidade
ax[1].plot(t_vals, v_vals, label="v(t) = ds/dt = 10t + 3", color='orange')
ax[1].set_title('Velocidade')
ax[1].set_xlabel('Tempo (s)')
ax[1].set_ylabel('Velocidade (m/s)')
ax[1].legend()
ax[1].grid(True)

# Plotar a função de aceleração
ax[2].plot(t_vals, a_vals, label="a(t) = dv/dt = 10", color='red')
ax[2].set_title('Aceleração')
ax[2].set_xlabel('Tempo (s)')
ax[2].set_ylabel('Aceleração (m/s²)')
ax[2].legend()
ax[2].grid(True)

# Ajustar o layout
plt.tight_layout()

# Mostrar o gráfico
plt.show()