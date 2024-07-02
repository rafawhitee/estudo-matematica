## OBS: o Baricentro é o encontro das retas das medianas dos 3 pontos do triângulo
## A Mediana divide o outro lado igual em partes, exemplo: se um lado tem total de 8, ao dividir por uma mediana, fica 4 em cada lado.
## E dividindo todos os lados com mediana, o encontro no centro desse triângulo é o baricentro

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