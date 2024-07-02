## 3 Pontos estarão alinhados quando o determinada de suas coordenadas forem iguais a 0

# Fórmula do baricentro
def baricentro(p1, p2, p3):
    return (p1 + p2 + p3)/3

# Coordenadas de um Triângulo
A = (3,8)
B = (6,8)
C = (3,12)

# Substituindo os valores
print(f"Baricentro - Eixo X: {baricentro(A[0], B[0], C[0])}")
print(f"Baricentro - Eixo Y: {baricentro(A[1], B[1], C[1])}")