import sympy as sp

# Definindo as variáveis
x, y = sp.symbols('x y')

# Definindo as equações
eq_1 = sp.Eq(1, 2*x + 3*y) # 2x + 3y = 1
eq_2 = sp.Eq(-2, 4*x + y) # 4x + y = -2

# Resolvendo o sistema de equações
print(f"Solução: {sp.solve((eq_1, eq_2))}")