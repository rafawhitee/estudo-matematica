import sympy as sp

# calcula a distância euclidiana entre 2 pontos
def distancia_euclidiana(A, B):
    x1, y1, x2, y2 = sp.symbols('x1 y1 x2 y2')
    expression = sp.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return expression.subs({x1: A[0], y1: B[0], x2: A[1], y2: B[1]}).evalf()

# calcula a distância do ponto para a reta
# OBS: a expressão da reta deve estar na forma geral --> Ax + By + C
def distancia_reta_ponto(reta_forma_geral, P):
    x, y = sp.symbols('x y')
    A = reta_forma_geral.coeff(x)
    B = reta_forma_geral.coeff(y)
    C = reta_forma_geral - A*x - B*y # C é o termo constante, então subtraímos as partes de x e y da expressão original
    return sp.Abs(((A * P[0]) + (B * P[1])  + C) / sp.sqrt(A**2 + B**2))

# retorna o menor ângulo (agudo) entre as 2 retas
def angulo_agudo(reta_forma_reduzida_1, reta_forma_reduzida_2):
    x = sp.symbols('x')
    coeficiente_angular_reta_1 = reta_forma_reduzida_1.coeff(x)
    coeficiente_angular_reta_2 = reta_forma_reduzida_2.coeff(x)
    if coeficiente_angular_reta_1 == 0:
        return sp.Abs(1 / coeficiente_angular_reta_2)
    if coeficiente_angular_reta_2 == 0:
        return sp.Abs(1 / coeficiente_angular_reta_1)
    return sp.Abs( (coeficiente_angular_reta_1 - coeficiente_angular_reta_2) / (1 + (coeficiente_angular_reta_1 * coeficiente_angular_reta_2) ))

# retorna o valor do coeficiente angular para a reta ser perpendicular
def coeficiente_angular_para_ser_perpendicular(reta_forma_reduzida):
    x = sp.symbols('x')
    return -(1/reta_forma_reduzida.coeff(x))

# retorna true ou false se as 2 retas são paralelas paralelas (formam um ângulo de 90 graus)
# OBS: a expressão da reta deve estar na forma reduzida --> y = Ax + B
def perpendiculares(reta_forma_reduzida_1, reta_forma_reduzida_2):
    x = sp.symbols('x')
    return reta_forma_reduzida_1.coeff(x) * reta_forma_reduzida_2.coeff(x) == -1

# retorna true ou false se as 2 retas são paralelas coincidentes (coeficiente angular e linear são iguais)
# OBS: a expressão da reta deve estar na forma reduzida --> y = Ax + B
def coincidentes(reta_forma_reduzida_1, reta_forma_reduzida_2):
    if paralelas(reta_forma_reduzida_1, reta_forma_reduzida_2):
        x = sp.symbols('x')
        # coeficiente linear é o termo constante, então subtraímos as partes de x da expressão original
        coeficiente_linear_reta_1 = reta_forma_reduzida_1 - reta_forma_reduzida_1.coeff(x)*x 
        coeficiente_linear_reta_2 = reta_forma_reduzida_2 - reta_forma_reduzida_2.coeff(x)*x 
        return coeficiente_linear_reta_1 == coeficiente_linear_reta_2
    return False

# retorna true ou false se as 2 retas são paralelas
# OBS: a expressão da reta deve estar na forma reduzida --> y = Ax + B
def paralelas(reta_forma_reduzida_1, reta_forma_reduzida_2):
    x = sp.symbols('x')
    return reta_forma_reduzida_1.coeff(x) == reta_forma_reduzida_2.coeff(x)

# retorna a coordenada do ponto médio entre os 2 pontos
def ponto_medio(A, B):
    return ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)

# retorna a coordenada do baricentro do triângulo (centro de gravidade)
def baricentro(A, B, C):
    return ((A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3)

# retorna a função python da Equação Geral da reta que passa pelos pontos A, B 
def equacao_geral_lambdify(A, B):
    return sp.lambdify(sp.symbols('x y'), equacao_geral(A, B), 'numpy')

# retorna a expressão da Equação Geral da reta que passa pelos pontos A, B 
def equacao_geral(A, B):
    x, y = sp.symbols('x y')
    coef_angular = coeficiente_angular(A, B)
    return y - A[1] - (coef_angular * (x - A[0]))

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