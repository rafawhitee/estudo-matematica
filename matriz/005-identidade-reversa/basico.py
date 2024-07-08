import sympy as sp

# matriz identidade de ordem 2
A = sp.Matrix([[1, 0],
                [0, 1]])
print(f"Matriz identidade de ordem 2: {A}")

# matriz identidade de ordem 3
B = sp.Matrix([[1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]])
print(f"Matriz identidade de ordem 3: {B}")

# Agora a inversa
# A multiplicação da original com sua inversa deve ser igual a identidade de mesma ordem
a, b, c, d = sp.symbols('a b c d')

# como é uma quadrada de ordem 2 (2 linhas e 2 colunas)
# deve ser igual a matriz identidade de ordem 2 (que é o A acima)
C = sp.Matrix([[2, 0],
                [4, -3]])

C_inversa = sp.Matrix([[a, b], 
                       [c, d]])

# a matriz original multiplicada por sua inversa, deve ser igual a matriz identidade de mesma ordem
equacao_inversa = sp.Eq(A, C * C_inversa)
solucao = sp.solve(equacao_inversa)
print(f"Solução da inversa: {solucao}")