import sympy as sp

# símbolos
x = sp.symbols('x')

log_natural = sp.log(x) # logaritmo natural (neuperiana)
funcao_natural = sp.lambdify(x, log_natural, 'numpy')

log_base_binaria = sp.log(x, 2) # logaritmo na base 2 (binária)
funcao_base_binaria = sp.lambdify(x, log_base_binaria, 'numpy')

log_base_decimal = sp.log(x, 10) # logaritmo na base 10 (decimal)
funcao_base_decimal = sp.lambdify(x, log_base_decimal, 'numpy')