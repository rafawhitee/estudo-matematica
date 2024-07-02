import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, integrate, lambdify

# Define a variável
x = symbols('x')

# Define a expressão
expression = x**2 - 3*x

# gera os valores de X
x_vals = np.linspace(-10, 40, 400)

# Calcula a derivada
derivative = diff(expression, x)

# Calcula a Integral da função original
integrate_expression = integrate(expression, x)

# Calcula a integral da derivada
integrate_derivative = integrate(derivative, x)

# Converter as expressões simbólicas para funções numéricas
expression_func = lambdify(x, expression, 'numpy')
derivative_func = lambdify(x, derivative, 'numpy')
integrate_expression_func = lambdify(x, integrate_expression, 'numpy')
integrate_derivative_func = lambdify(x, integrate_derivative, 'numpy')

# Criar a figura e os eixos
fig, ax = plt.subplots()

ax.plot(x_vals, expression_func(x_vals), label="Expressão Original")
ax.plot(x_vals, derivative_func(x_vals), label="Derivada da Original")
ax.plot(x_vals, integrate_expression_func(x_vals), label="Integral da Original")
ax.plot(x_vals, integrate_derivative_func(x_vals), label="Integral da Derivada")

# Configurar o plano cartesiano
ax.axhline(y=0, color='k')  # Eixo x
ax.axvline(x=0, color='k')  # Eixo y
ax.grid(True, which='both')

# Adicionar título e legendas
plt.title('Função, suas Derivadas e Integrais')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

# Definir os limites dos eixos
ax.set_xlim([-2, 4])
ax.set_ylim([-10, 10])

# Mostrar o gráfico
plt.show()