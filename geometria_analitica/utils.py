import sympy as sp

x1, y1 = sp.symbols('x1 y1')
x2, y2 = sp.symbols('x2 y2')

_distancia_euclidiana = sp.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def distancia_euclidiana(A, B):
    return _distancia_euclidiana.subs({x1: A[0], y1: B[0], x2: A[1], y2: B[1]}).evalf()