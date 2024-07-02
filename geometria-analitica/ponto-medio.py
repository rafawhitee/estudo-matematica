# Fórmula do ponto médio
def ponto_medio(p1, p2):
    return (p1 + p2)/2

# Coordenadas 
A = (3,8)
B = (6,8)
C = (3,12)
D = (10,19)

# Substituindo os valores
print(f"Ponto Médio do Eixo X entre AB: {ponto_medio(A[0], B[0])}")
print(f"Ponto Médio do Eixo Y entre AB: {ponto_medio(A[1], B[1])} \n")

print(f"Ponto Médio do Eixo X entre AC: {ponto_medio(A[0], C[0])}")
print(f"Ponto Médio do Eixo Y entre AC: {ponto_medio(A[1], C[1])} \n")

print(f"Ponto Médio do Eixo X entre AD: {ponto_medio(A[0], D[0])}")
print(f"Ponto Médio do Eixo Y entre AD: {ponto_medio(A[1], D[1])} \n")

print(f"Ponto Médio do Eixo X entre BC: {ponto_medio(B[0], C[0])}")
print(f"Ponto Médio do Eixo Y entre BC: {ponto_medio(B[1], C[1])} \n")

print(f"Ponto Médio do Eixo X entre BD: {ponto_medio(B[0], D[0])}")
print(f"Ponto Médio do Eixo Y entre BD: {ponto_medio(B[1], D[1])} \n")

print(f"Ponto Médio do Eixo X entre CD: {ponto_medio(C[0], D[0])}")
print(f"Ponto Médio do Eixo Y entre CD: {ponto_medio(C[1], D[1])}")