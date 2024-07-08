import sympy as sp

# declara o símbolo X
x = sp.symbols('x')

# cria como expressão (x é a quantidade de livros)
expressao = 70*x
funcao = sp.lambdify(x, expressao, 'numpy') # transforma em função

print(f"Valor para 1 livro -->  R$ {funcao(1)} ")
print(f"Valor para 2 livros --> R$ {funcao(2)}")
print(f"Valor para 3 livros --> R$ {funcao(3)}")

# cria uma nova expressão (x é o valor) e 15 reais é o frete
expressao_com_frete = 70*x + 15
funcao_com_frete = sp.lambdify(x, expressao_com_frete, 'numpy')

print(f"Valor para 1 livro com frete -->  R$ {funcao_com_frete(1)} ")
print(f"Valor para 2 livros com frete --> R$ {funcao_com_frete(2)}")
print(f"Valor para 3 livros com frete --> R$ {funcao_com_frete(3)}")

