import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

dados = pd.read_csv('src/parte2/dados.csv')

# faz a query no csv para pegar todos que tem até 5000 de renda
rendas_5000 = dados.query('Renda <= 5000').Renda

# Estamos estudando o rendimento mensal dos chefes de domicílios com renda até R$ 5.000,00 no Brasil. 
# Nosso supervisor determinou que o erro máximo em relação a média seja de R$ 10,00. 
# Sabemos que o desvio padrão populacional deste grupo de trabalhadores é de R$ 1.082,79 e que a média populacional é de R$ 1.426,54. 
# Para um nível de confiança de 95%, qual deve ser o tamanho da amostra de nosso estudo? 
# Qual o intervalo de confiança para a média considerando o tamanho de amostra obtido?

# Erro inferencial
e = 10 # R$ 10

# Desvio Padrão Populacional (deu o valor no enunciado)
desvio_padrao_populacional = 1082.79 # R$ 1082,79

# Média Populacional (deu o valor no enunciado)
media_populacional = 1426.54 # R$ 1426,54

# Nível de Significância
significania = 0.05 # 5%

# Nível de Confiança (1 - Significância)
confianca = 1 - significania

# calcula a probabilidade até o limite superior
# como é uma distribuição normal, é simétrico
# então por isso divide a confianca em 2 (95% fica 47,5% para cada lado)
# então no lado direito tem 47,5% e do meio (média) até o menos infinito, sabe que é 50%, então fica 47,5% + 50.0% totalizando 97.5%
probabilidade_ate_limite_superior = (confianca / 2) + 0.5
Z = norm.ppf(probabilidade_ate_limite_superior)

n = (Z * (desvio_padrao_populacional / e)) ** 2
n = int(n.round())
print(f"N: {n}")

intervalo = norm.interval(confidence = confianca, loc = media_populacional, scale = desvio_padrao_populacional / np.sqrt(n))
print(f"Intervalo: {intervalo}")

# Realizando uma prova/análise gráfica

tamanho_simulacao = 1000

medias = [rendas_5000.sample(n = n).mean() for i in range(1, tamanho_simulacao)]
medias = pd.DataFrame(medias)

ax = medias.plot(style = '.')
ax.figure.set_size_inches(12, 6)
ax.hlines(y = media_populacional, xmin = 0, xmax = tamanho_simulacao, colors='black', linestyles='dashed')
ax.hlines(y = intervalo[0], xmin = 0, xmax = tamanho_simulacao, colors='red', linestyles='dashed')
ax.hlines(y = intervalo[1], xmin = 0, xmax = tamanho_simulacao, colors='red', linestyles='dashed')
plt.show()