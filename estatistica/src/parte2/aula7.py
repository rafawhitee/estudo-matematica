import numpy as np
from scipy.stats import norm



####### OBSERVAÇÃO #########
#  EM CASO DE DÚVIDAS, OLHAR AS FÓRMULAS DO NO CURSO_DE_ESTATISTICA_PARTE_2.ipynb (PARTE DE INTERVALO DE CONFIANÇA)
####### OBSERVAÇÃO #########

# Suponha que os pesos dos sacos de arroz de uma indústria brasileira alimentícia 
# se distribuem aproximadamente como uma normal de desvio padrão populacional igual a 150 gramas.
# Selecionada uma amostra aleatório de 20 sacos de um lote específico, obteve-se um peso médio de 5050 gramas. 
# Construa um intervalo de confiança para a média populacional assumindo um nível de significância de 5%

# Desvio Padrão Populacional (deu o valor no enunciado)
desvio_padrao_populacional = 150 # gramas

# Tamanho da amostra (deu o valor no enunciado)
n = 20 # os 20 sacos de um lote específico
raiz_quadrada_n = np.sqrt(n) # raiz quadrada do n

# Média da Amostra (deu o valor no enunciado)
media_amostra = 5050 # gramas

# Nível de Significância (deu o valor no enunciado de 5%)
# representa a probabilidade de erro da estimativa
significania = 0.05 # 5%

# Nível de Confiança (1 - Significância)
# representa a probabilidade de acerto da estimativa
confianca = 1 - significania

# calcula a probabilidade até o limite superior
# como é uma distribuição normal, é simétrico
# então por isso divide a confianca em 2 (95% fica 47,5% para cada lado)
# então no lado direito tem 47,5% e do meio (média) até o menos infinito, sabe que é 50%, então fica 47,5% + 50.0% totalizando 97.5%
probabilidade_ate_limite_superior = (confianca / 2) + 0.5

Z = norm.ppf(probabilidade_ate_limite_superior)
print(f"Z: {Z}")

# Obtendo o Sigma (Teorema do Limite Central, explicado na aula anterior, aula21.py)
sigma = desvio_padrao_populacional / raiz_quadrada_n
print(f"Sigma (Teorema do Limite Central): {sigma}")

# Obtendo o E (erro inferencial)
e = Z * sigma
print(f"Erro inferencial: {e} gramas")

# Calculando o Intervalo de confiança (Manual e pelo Scipy)
intervalo_manual = (media_amostra - e, media_amostra + e)
print(f"Intervalo de Confiança (cálculo manual): {intervalo_manual}")

intervalo_scipy = norm.interval(confidence = confianca, loc = media_amostra, scale = sigma)
print(f"Intervalo de Confiança (scipy): {intervalo_scipy}")