import sympy as sp

# calcula a distância euclidiana entre 2 pontos
def distancia_euclidiana(A, B):
    x1, y1 = sp.symbols('x1 y1')
    x2, y2 = sp.symbols('x2 y2')
    expression = sp.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return expression.subs({x1: A[0], y1: B[0], x2: A[1], y2: B[1]}).evalf()

# retorna a coordenada do ponto médio entre os 2 pontos
def ponto_medio(A, B):
    return ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)

# retorna a coordenada do baricentro do triângulo (centro de gravidade)
def baricentro(A, B, C):
    return ((A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3)

# retorna a função python da Equação Reduzida Invertida da reta que passa pelos pontos A, B 
# Ex: imagina a expressão 'y = 2x - 3', a sua invertida é 'x = (y - 3) / 2'
def equacao_reduzida_invertida_lambdify(A, B):
     return sp.lambdify(sp.symbols('y'), equacao_reduzida_invertida(A, B), 'numpy')

# retorna a expressão da Equação Reduzida Invertida da reta que passa pelos pontos A, B 
# Ex: imagina a expressão 'y = 2x - 3', a sua invertida é 'x = (y - 3) / 2'
def equacao_reduzida_invertida(A, B):
    coef_angular = coeficiente_angular(A, B)
    # valida se o coeficiente angular não é 0
    # se for, a expressão é constante, basta saber qual a constante
    if coef_angular == 0:
        return A[0] if A[0] == B[0] else A[1]
    return (sp.symbols('y') - coeficiente_linear(A, B)) / coef_angular

# retorna a função python da Equação Reduzida da reta que passa pelos pontos A, B 
def equacao_reduzida_lambdify(A, B):
    return sp.lambdify(sp.symbols('x'), equacao_reduzida(A, B), 'numpy')

# retorna a expressão da Equação Reduzida da reta que passa pelos pontos A, B 
def equacao_reduzida(A, B):
    return (coeficiente_angular(A, B) * sp.symbols('x')) + coeficiente_linear(A, B)

# retorna o coeficiente linear entre a reta dos 2 pontos
def coeficiente_linear(A, B):
    return A[1] - (coeficiente_angular(A, B) * A[0])

# retorna o coeficiente angular (declividade da reta) entre a reta dos 2 pontos
def coeficiente_angular(A, B):
    diferenca_eixo_x = B[0] - A[0]
    if diferenca_eixo_x == 0:
        return 0
    return (B[1] - A[1]) / diferenca_eixo_x