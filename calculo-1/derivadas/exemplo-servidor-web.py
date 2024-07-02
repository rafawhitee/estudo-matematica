import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, lambdify

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

# Criar a figura e os eixos
fig, ax = plt.subplots()

# Plotar a função tempo de resposta
ax.plot(N_vals, T_vals, label='Tempo de Resposta T(N)')

# Marcar o ponto crítico
ax.plot(N_critical, T_critical, 'ro')
ax.annotate(f'Número Ótimo de Servidores: {N_critical:.2f}', xy=(N_critical, T_critical), xytext=(N_critical, T_critical + 10),
            textcoords='offset points', arrowprops=dict(facecolor='black', arrowstyle='->'), ha='center')

# Configurar o plano cartesiano
ax.axhline(y=0, color='k')  # Eixo x
ax.axvline(x=0, color='k')  # Eixo y
ax.grid(True, which='both')

# Adicionar título e legendas
plt.title('Otimização do Tempo de Resposta')
plt.xlabel('Número de Servidores (N)')
plt.ylabel('Tempo de Resposta (T)')
plt.legend()
plt.grid(True)

# Definir os limites dos eixos
ax.set_xlim([1, 20])
ax.set_ylim([-10, max(T_vals) + 50])

# Mostrar o gráfico
plt.show()