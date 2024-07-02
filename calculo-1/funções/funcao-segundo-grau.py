import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, Eq, solve

# declara o símbolo X
x = symbols('x')

# cria valores para X
x_vals = np.linspace(-10, 10, 400)

# cria como expressão
expression = 2*x**2 + 5*x - 12

# mostra um exemplo com X = 2
print(f"Resultado de '2x² + 5x - 12' com x = 2: {expression.subs(x, 2)}") 

# cria como equação
equation = Eq(expression, 0)

# raiz da função
print(f"Raiz da Função '2x² + 5x - 12': {solve(equation, x)}") 

# converte a expressão para uma função numérica
expression_func = lambdify(x, expression, 'numpy')

# a partir dos valores de X, joga na expressão para retornar o Y para poder mostrar o gráfico
y_vals = expression_func(x_vals)

# cria a figura e os eixos
fig, ax = plt.subplots()

# adiciona o plot da função dentro do eixo do plano cartesiano
ax.plot(x_vals, y_vals, label=f'{expression}')

# configura o plano cartesiano
ax.axhline(y=0, color='k')  # Eixo x
ax.axvline(x=0, color='k')  # Eixo y
ax.grid(True, which='both')

# faz o plot
plt.title('Função do Segundo Grau')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

ax.set_xlim([-10, 10])
ax.set_ylim([min(y_vals) - 5, max(y_vals) + 5])

# mostrar o gráfico
plt.show()