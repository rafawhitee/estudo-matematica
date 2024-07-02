import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Definir símbolos
x, y = sp.symbols('x y')

# Definir duas retas
reta1 = sp.Eq(2*x - y, 1)  # 2x - y = 1
reta2 = sp.Eq(x + y, 5)    # x + y = 5

# Encontrar a interseção das retas
intersecao = sp.solve((reta1, reta2), (x, y))
print(f"Interseção das retas: {intersecao}")

# Definir um ponto
ponto = (4, 5)

# Encontrar a distância do ponto à reta1
distancia = sp.Abs(reta1.lhs.subs(x, ponto[0]).subs(y, ponto[1]) - reta1.rhs) / sp.sqrt(reta1.lhs.coeff(x)**2 + reta1.lhs.coeff(y)**2)
distancia = sp.simplify(distancia)
print(f"Distância do ponto {ponto} à reta 2x - y = 1: {distancia}")

# Encontrar o ângulo entre as retas
coef1 = reta1.lhs.coeff(x), reta1.lhs.coeff(y)
coef2 = reta2.lhs.coeff(x), reta2.lhs.coeff(y)
produto_escalar = coef1[0]*coef2[0] + coef1[1]*coef2[1]
magnitude1 = sp.sqrt(coef1[0]**2 + coef1[1]**2)
magnitude2 = sp.sqrt(coef2[0]**2 + coef2[1]**2)
cos_theta = produto_escalar / (magnitude1 * magnitude2)
angulo = sp.acos(cos_theta)
angulo = sp.deg(angulo)  # Convertendo para graus
print(f"Ângulo entre as retas: {angulo.evalf()} graus")

# Visualizar as retas e o ponto
x_vals = np.linspace(-2, 5, 100)
reta1_y_vals = (2*x_vals - 1)
reta2_y_vals = (5 - x_vals)

plt.plot(x_vals, reta1_y_vals, label='2x - y = 1')
plt.plot(x_vals, reta2_y_vals, label='x + y = 5')
plt.scatter(*ponto, color='red', label='Ponto (2, 3)')
plt.scatter(*intersecao.values(), color='green', label='Interseção')

plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.title('Geometria Analítica com SymPy')
plt.show()
