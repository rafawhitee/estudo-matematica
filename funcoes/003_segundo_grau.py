import numpy as np
import sympy as sp
from plano_cartesiano.utils import PlanoCartesiano

# declara o símbolo X
x = sp.symbols('x')

# cria valores para X
x_vals = np.linspace(-10, 10, 400)

# cria a primeira função do segundo grau
coeficiente_a = 2
coeficiente_b = 5
coeficiente_c = -12
expressao = coeficiente_a*x**2 + coeficiente_b*x - coeficiente_c # 2x² + 5x - 12
funcao = sp.lambdify(x, expressao, 'numpy')

print(f"Resultado de '2x² + 5x - 12' com x = 2: {funcao(2)}") 

# ponto mínimo ou máximo da primeira função (como o A > 0, é ponto mínimo)
x_ponto_min_ou_max = -coeficiente_b/(2*coeficiente_a)
y_ponto_min_ou_max = funcao(x_ponto_min_ou_max)
coordenada_ponto_min_ou_max = (x_ponto_min_ou_max, y_ponto_min_ou_max)

# cria a segunda função do segundo grau
coeficiente_a2 = -3
coeficiente_b2 = 2
coeficiente_c2 = 7
expressao_2 = coeficiente_a2*x**2 + coeficiente_b2*x - coeficiente_c2 # -3x² + 2x + 7
funcao_2 = sp.lambdify(x, expressao_2, 'numpy')

print(f"Resultado de '-3x² + 2x + 7' com x = 2: {funcao(2)}") 

# ponto mínimo ou máximo da primeira função (como o A < 0, é ponto máximo)
x_2_ponto_min_ou_max = -coeficiente_b2/(2*coeficiente_a2)
y_2_ponto_min_ou_max = funcao_2(x_2_ponto_min_ou_max)
coordenada_2_ponto_min_ou_max = (x_2_ponto_min_ou_max, y_2_ponto_min_ou_max)

# a partir dos valores de X, joga na expressão para retornar o Y para poder mostrar o gráfico
plano_cartesiano = PlanoCartesiano()

plano_cartesiano.inserir_pontos(valores_eixo_x=x_vals, valores_eixo_y=funcao(x_vals), label=f'{expressao}', cor="green")
plano_cartesiano.inserir_anotacao(coordenada=coordenada_ponto_min_ou_max, titulo="Ponto Mínimo")
plano_cartesiano.inserir_ponto(coordenada=coordenada_ponto_min_ou_max, cor="yellow")

plano_cartesiano.inserir_pontos(valores_eixo_x=x_vals, valores_eixo_y=funcao_2(x_vals), label=f'{expressao_2}', cor="red")
plano_cartesiano.inserir_anotacao(coordenada=coordenada_2_ponto_min_ou_max, titulo="Ponto Máximo")
plano_cartesiano.inserir_ponto(coordenada=coordenada_2_ponto_min_ou_max, cor="blue")

plano_cartesiano.alterar_limites_eixos([min(x_vals) - 5, max(x_vals) + 5], [-250, 250])
plano_cartesiano.renderizar()