import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, lambdify

# Definir a variável e a função
x = symbols('x')
expression = x**2 - 3*x

# Calcular a derivada
derivative = diff(expression, x)

# Converter as expressões simbólicas para funções numéricas
expression_func = lambdify(x, expression, 'numpy')
derivative_func = lambdify(x, derivative, 'numpy')

# Criar um intervalo de valores para x
x_vals = np.linspace(-10, 10, 1000)
y_vals = expression_func(x_vals)
dy_vals = derivative_func(x_vals)

# Ponto específico para a linha tangente
a = 4
tangent_line = derivative_func(a) * (x_vals - a) + expression_func(a)

# Criar a figura e os eixos
fig, ax = plt.subplots()

# Plotar a função original
ax.plot(x_vals, y_vals, label='f(x) = x^2 - 3x')

# Plotar a derivada
ax.plot(x_vals, dy_vals, label='f\'(x) = 2x - 3', linestyle='--')

# Plotar a linha tangente
ax.plot(x_vals, tangent_line, label=f'Tangente em x={a}', linestyle=':')

# Configurar o plano cartesiano
ax.axhline(y=0, color='k')  # Eixo x
ax.axvline(x=0, color='k')  # Eixo y
ax.grid(True, which='both')

# Adicionar título e legendas
plt.title('Função, sua Derivada e Linha Tangente')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

# Definir os limites dos eixos
ax.set_xlim([-2, 5])
ax.set_ylim([-10, 10])

# Mostrar o gráfico
plt.show()
