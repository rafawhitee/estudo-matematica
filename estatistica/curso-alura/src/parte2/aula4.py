from scipy.stats import norm

# Em um estudo sobre as alturas dos moradores de uma cidade verificou-se que o conjunto de dados segue uma distribuição aproximadamente normal,
# com média de 1,70 metros e o desvio padrão é de 0,1. Com estas informações obtenha o seguinte conjunto de probabilidades:

# A) Probabilidade de uma pessoa, selecionada ao acaso, ter menos de 1,8 metros.
# B) Probabilidade de uma pessoa, selecionada ao acaso, ter entre 1,60 e 1,80 metros.
# C) Probabilidade de uma pessoa, selecionada ao acaso, ter mais de 1,90 metros.

media = 1.7
desvio_padrao = 0.1

# 
# Resolvendo o Primeiro Caso (Letra A)
#
Z1 = (1.8 - media) / desvio_padrao
probabilidade_caso_a = norm.cdf(Z1)
print(f"Probabilidade do Primeiro Caso (menos de 1,80 metros): {probabilidade_caso_a * 100}%")


# 
# Resolvendo o Segundo Caso (Letra B)
#
Z_superior = (1.8 - media) / desvio_padrao
Z_inferior = (1.6 - media) / desvio_padrao
probabilidade_caso_b = norm.cdf(Z_superior) - norm.cdf(Z_inferior)
print(f"Probabilidade do Segundo Caso (entre 1,60 e 1,80 metros): {probabilidade_caso_b * 100}%")


# 
# Resolvendo o Terceiro Caso (Letra C)
#
Z2 = (1.9 - media) / desvio_padrao
probabilidade_caso_c = 1 - norm.cdf(Z2)
print(f"Probabilidade do Terceiro Caso (ter mais de 1.90 metros): {probabilidade_caso_c * 100}%")


Z = ()