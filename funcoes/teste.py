import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define a função f(x)
def f(x, a):
    return a * x

# Cria a figura e os eixos
fig, ax = plt.subplots()
x = np.linspace(-10, 10, 400)
line, = ax.plot(x, f(x, 2))

# Define a função de animação
def animate(i):
    print(f"animate i atual --> {i}")
    #ax.clear()
    a = i
    y = f(x, a)
    ax.plot(x, y)
    ax.set_xlim([-10, 10])
    ax.set_ylim([-20, 20])
    ax.set_title(f"y = {a}x")
    ax.grid(True)

# Cria a animação
ani = FuncAnimation(fig, animate, frames=[2, 4], interval=200)

# Mostra a animação
plt.show()
