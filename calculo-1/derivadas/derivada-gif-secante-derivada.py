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

# Ponto onde calcularemos a derivada e a secante
x0 = -2

# Intervalo para desenhar a função
x = np.linspace(-2, 4, 400)
y = quadratic_function(x, a, b, c)

# Configurando a figura e o eixo
fig, ax = plt.subplots()
line1, = ax.plot(x, y, label='Função Quadrática $f(x) = ax^2 + bx + c$')
line2, = ax.plot([], [], '--', label='Secante')
point, = ax.plot([], [], 'ro')
text = ax.text(x0, quadratic_function(x0, a, b, c), f'$x_0 = {x0}$')

# Configurações do eixo
ax.set_xlim(-2, 4)
ax.set_ylim(-1, 10)
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Função Quadrática e Aproximações de Secantes')
ax.legend()
ax.grid(True)

# Função de inicialização
def init():
    line2.set_data([], [])
    point.set_data([], [])
    return line2, point, text

# Função de animação
def animate(i):
    h = 1 / (2**i)
    secant_slope = (quadratic_function(x0 + h, a, b, c) - quadratic_function(x0, a, b, c)) / h
    secant_line = secant_slope * (x - x0) + quadratic_function(x0, a, b, c)
    line2.set_data(x, secant_line)
    point.set_data([x0], [quadratic_function(x0, a, b, c)])
    text.set_text(f'$x_0 = {x0}$, $h = {h:.4f}$')
    return line2, point, text

# Criando a animação
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=20, interval=500, blit=True)

# Salvando a animação como GIF
ani.save('secant_to_derivative.gif', writer='imagemagick')

plt.show()
