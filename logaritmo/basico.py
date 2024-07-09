import sympy as sp
import numpy as np

# símbolos
x = sp.symbols('x')

log_natural = sp.log(x) # logaritmo natural (neperiano)
funcao_natural = sp.lambdify(x, log_natural, 'numpy')
print(f"Se for a mesma o valor for igual a base, o resultado do logaritmo será igual a 1. \n  Exemplo de ln(constante_neperiano) --> {funcao_natural(np.e)} \n")

log_base_binaria = sp.log(x, 2) # logaritmo na base 2 (binária)
funcao_base_binaria = sp.lambdify(x, log_base_binaria, 'numpy')
print(f"Se for a mesma o valor for igual a base, o resultado do logaritmo será igual a 1. \n  Exemplo de log(2) na base 2 --> {funcao_base_binaria(2)} \n")

log_base_decimal = sp.log(x, 10) # logaritmo na base 10 (decimal)
funcao_base_decimal = sp.lambdify(x, log_base_decimal, 'numpy')
print(f"Se for a mesma o valor for igual a base, o resultado do logaritmo será igual a 1. \n  Exemplo de log(10) na base 10 --> {funcao_base_decimal(10)} \n")