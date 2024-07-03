import sympy as sp

def distancia_euclidiana(A, B):
    x1, y1 = sp.symbols('x1 y1')
    x2, y2 = sp.symbols('x2 y2')
    expression = sp.sqrt(sp.Abs((x2 - x1))**2 + sp.Abs((y2 - y1))**2)
    return expression.subs({x1: A[0], y1: B[0], x2: A[1], y2: B[1]}).evalf()

def ponto_medio(A, B):
    return ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)

def baricentro(A, B, C):
    return ((A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3)

def equacao_reduzida_lambdify(A, B):
    x = sp.symbols('x')
    return sp.lambdify(x, equacao_reduzida(A, B), 'numpy')

def equacao_reduzida(A, B):
    x = sp.symbols('x')
    return coeficiente_angular(A, B) * x + coeficiente_linear(A, B)

def coeficiente_linear(A, B):
    return A[1] - coeficiente_angular(A, B) * A[0]

def coeficiente_angular(A, B):
    return sp.Abs((B[1] - A[1])) / sp.Abs((B[0] - A[0]))