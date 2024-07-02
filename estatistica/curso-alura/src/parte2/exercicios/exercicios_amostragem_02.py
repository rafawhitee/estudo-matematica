import numpy as np
from scipy.stats import norm

# Uma amostra aleatória simples de 1976 itens de uma população normalmente distribuída, com desvio padrão populacional igual a 11, 
# resultou em uma média amostral de 28.
# Qual o intervalo de confiança de 90% para a média populacional?

# desvio padrão 
desvio_padrao = 11 

# media amostral
media_amostral = 28 

# tamanho da amostra
n = 1976
raiz_quadrada_n = np.sqrt(n)

# Nível de Significância
significania = 0.10 # 10%

# Nível de Confiança (1 - Significância)
confianca = 1 - significania # 90%

# probabilidade até o limite superior (no caso o Z superior)
probabilidade_ate_limite_superior = (confianca / 2) + 0.5
Z = norm.ppf(probabilidade_ate_limite_superior)

# calculando o sigma (teorema do limite central)
sigma = desvio_padrao / raiz_quadrada_n

# Obtendo o E (erro inferencial)
e = Z * sigma

intervalo_scipy = norm.interval(confidence = confianca, loc = media_amostral, scale = sigma)
print(f"Intervalo de Confiança (scipy): {intervalo_scipy}")
