import numpy as np
from scipy.stats import norm

# Para estimar o valor médio gasto por cada cliente de uma grande rede de fast-food, foi selecionada uma amostra de 50 clientes.
# Assumindo que o valor do desvio padrão da população seja de R$ 6,00 e que esta população se distribui normalmente, 
# obtenha a margem de erro desta estimativa para um nível de confiança de 95%.

# desvio padrão
desvio_padrao = 6 

# tamanho da amostra
n = 50
raiz_quadrada_n = np.sqrt(n)

# Nível de Significância
significania = 0.05 # 5%

# Nível de Confiança (1 - Significância)
confianca = 1 - significania # 95%

# probabilidade até o limite superior (no caso o Z superior)
probabilidade_ate_limite_superior = (confianca / 2) + 0.5
Z = norm.ppf(probabilidade_ate_limite_superior)

# calculando o sigma (teorema do limite central)
sigma = desvio_padrao / raiz_quadrada_n

# Obtendo o E (erro inferencial)
e = Z * sigma

print(f"Margem de erro: R$ {e}")
