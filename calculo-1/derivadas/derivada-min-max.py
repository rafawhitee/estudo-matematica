import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, lambdify, solve

# Definir a variável e a função
x = symbols('x')
expression = x**3 - 6*x**2 + 9*x + 1

# Calcular a primeira e segunda derivada
first_derivative = diff(expression, x)
second_derivative = diff(first_derivative, x)

# Converter as expressões simbólicas para funções numéricas
expression_func = lambdify(x, expression, 'numpy')
first_derivative_func = lambdify(x, first_derivative, 'numpy')
second_derivative_func = lambdify(x, second_derivative, 'numpy')

# Criar um intervalo de valores para x
x_vals = np.linspace(-1, 5, 400)
y_vals = expression_func(x_vals)
dy_vals = first_derivative_func(x_vals)
ddy_vals = second_derivative_func(x_vals)

# Calcular os pontos críticos
critical_points = solve(first_derivative, x)

# Calcular os valores da função nos pontos críticos
critical_values = [expression_func(cp.evalf()) for cp in critical_points]

# Criar a figura e os eixos
fig, ax = plt.subplots()

# Plotar a função original
ax.plot(x_vals, y_vals, label='f(x) = x^3 - 6x^2 + 9x + 1')

# Plotar a primeira derivada
ax.plot(x_vals, dy_vals, label="f'(x) = 3x^2 - 12x + 9", linestyle='--')

# Plotar a segunda derivada
ax.plot(x_vals, ddy_vals, label="f''(x) = 6x - 12", linestyle=':')

# Marcar os pontos críticos
for cp, cv in zip(critical_points, critical_values):
    ax.plot(cp, cv, 'ro' if second_derivative_func(cp) < 0 else 'go')
    ax.annotate(f'{cp}', xy=(cp, cv), xytext=(cp, cv+5), textcoords='offset points', ha='center')

# Configurar o plano cartesiano
ax.axhline(y=0, color='k')  # Eixo x
ax.axvline(x=0, color='k')  # Eixo y
ax.grid(True, which='both')

# Adicionar título e legendas
plt.title('Máximos e Mínimos de uma Função Usando Derivadas')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

# Definir os limites dos eixos
ax.set_xlim([-1, 5])
ax.set_ylim([-10, 10])

# Mostrar o gráfico
plt.show()