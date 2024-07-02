from scipy.stats import norm

# O faturamento diário de um motorista de aplicativo segue uma distribuição aproximadamente normal, com média R$ 300,00 e desvio padrão igual a R$ 50,00. 
# Obtenha as probabilidades de que, em um dia aleatório, o motorista ganhe:
# A) Entre R$ 250,00 e R$ 350,00
# B) Entre R$ 400,00 e R$ 500,00

media = 300
desvio_padrao = 50

# 
# Resolvendo o Primeiro Caso (Letra A)
#
Z_superior_caso_a = (350 - media) / desvio_padrao
Z_inferior_caso_a = (250 - media) / desvio_padrao
probabilidade_caso_a = norm.cdf(Z_superior_caso_a) - norm.cdf(Z_inferior_caso_a)
print(f"Probabilidade do Primeiro Caso (entre R$250 e R$350): {probabilidade_caso_a * 100}%")

# 
# Resolvendo o Segundo Caso (Letra B)
#
Z_superior_caso_b = (500 - media) / desvio_padrao
Z_inferior_caso_b = (400 - media) / desvio_padrao
probabilidade_caso_b = norm.cdf(Z_superior_caso_b) - norm.cdf(Z_inferior_caso_b)
print(f"Probabilidade do Segundo Caso (entre R$400 e R$500): {probabilidade_caso_b * 100}%")