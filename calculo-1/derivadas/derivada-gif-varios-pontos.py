import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Definindo a função quadrática
def quadratic_function(x, a, b, c):
    return a * x**2 + b * x + c

# Definindo a derivada da função quadrática
def quadratic_derivative(x, a, b):
    return 2 * a * x + b

# Parâmetros da função quadrática
a = 1
b = -2
c = 1

# Intervalo para desenhar a função
x = np.linspace(-2, 4, 400)
y = quadratic_function(x, a, b, c)

# Configurando a figura e o eixo
fig, ax = plt.subplots()
line1, = ax.plot(x, y, label='Função Quadrática $f(x) = ax^2 + bx + c$')
line2, = ax.plot([], [], '--', label='Tangente')
point, = ax.plot([], [], 'ro')

# Configurações do eixo
ax.set_xlim(-2, 4)
ax.set_ylim(-1, 10)
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Função Quadrática e sua Derivada em Vários Pontos')
ax.legend()
ax.grid(True)

# Função de inicialização
def init():
    line2.set_data([], [])
    point.set_data([], [])
    return line2, point

# Função de animação
def animate(i):
    x0 = -2 + 6 * (i / 100)  # Movendo x0 de -2 a 4
    tangent_slope = quadratic_derivative(x0, a, b)
    tangent_line = tangent_slope * (x - x0) + quadratic_function(x0, a, b, c)
    line2.set_data(x, tangent_line)
    point.set_data([x0], [quadratic_function(x0, a, b, c)])
    return line2, point

# Criando a animação
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=144, interval=200, blit=True)

# Salvando a animação como GIF
ani.save('quadratic_with_derivative.gif', writer='imagemagick')

plt.show()
