import sympy as sp

# Definindo as variáveis
x, y, z, u = sp.symbols('x y z u')

# Definindo as equações com 3 variáveis
eq_1 = sp.Eq(3, 5*x + 3*y + z) # 5x + 3y + z = 3
eq_2 = sp.Eq(4, 3*x + -1*y - 3*z) # 3x - 1y - 3z = 4
eq_3 = sp.Eq(2, x + y - 2*z) # x + y - 2z = 2

# Resolvendo o sistema de equações
print(f"Solução do Sistema com as Equações 1, 2 e 3: {sp.solve((eq_1, eq_2, eq_3))}")

# Definindo as equações com 4 variáveis
eq_4 = sp.Eq(12, 2*x + 5*y + z - u) # 2x + 5y + z - u = 12
eq_5 = sp.Eq(7, x + -2*y - 3*z - 2*u) # x - 2y - 3z - 2u = 7
eq_6 = sp.Eq(9, x + y - 2*z + 3*u) # x + y - 2z + 3u = 9
eq_7 = sp.Eq(-5, 2*x - 1*y - 2*z + u) # x + y - 2z = -5

# Resolvendo o sistema de equações
print(f"Solução do Sistema com as Equações 1, 2 e 3: {sp.solve((eq_4, eq_5, eq_6, eq_7))}")