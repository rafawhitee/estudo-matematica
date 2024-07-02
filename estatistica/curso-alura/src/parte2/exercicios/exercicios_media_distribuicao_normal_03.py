from scipy.stats import norm

# O Inmetro verificou que as lâmpadas incandescentes da fabricante XPTO apresentam uma vida útil normalmente distribuída, 
# com média igual a 720 dias e desvio padrão igual a 30 dias. Calcule a probabilidade de uma lâmpada, escolhida ao acaso, durar:
# A) Entre 650 e 750 dias
# B) Mais que 800 dias
# C) Menos que 700 dias

media = 720
desvio_padrao = 30

# 
# Resolvendo o Primeiro Caso (Letra A)
#
Z_superior_caso_a = (750 - media) / desvio_padrao
Z_inferior_caso_a = (650 - media) / desvio_padrao
probabilidade_caso_a = norm.cdf(Z_superior_caso_a) - norm.cdf(Z_inferior_caso_a)
print(f"Probabilidade do Primeiro Caso (entre 650 e 750 dias): {probabilidade_caso_a * 100}%")

# 
# Resolvendo o Segundo Caso (Letra B)
#
Z_caso_b = (800 - media) / desvio_padrao
probabilidade_caso_b = 1 - norm.cdf(Z_caso_b) 
print(f"Probabilidade do Segundo Caso (mais que 800 dias): {probabilidade_caso_b * 100}%")

# 
# Resolvendo o Terceiro Caso (Letra C)
#
Z_caso_c = (700 - media) / desvio_padrao
probabilidade_caso_c = norm.cdf(Z_caso_c) 
print(f"Probabilidade do Terceiro Caso (menos que 700 dias): {probabilidade_caso_c * 100}%")