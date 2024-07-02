import numpy as np
from scipy.stats import norm

# Um fabricante de farinha afirma que a quantidade média de farinha nas embalagens de seu principal produto é de 500 g. 
# Um teste de pesagem em 30 embalagens amostradas ao acaso mostrou um peso médio igual à 485 g. 
# Estudos anteriores afirmam que a distribuição dos pesos segue uma distribuição normal e que o desvio padrão populacional é igual a 20 g. 
# Considerando um nível de significância igual a 5%, responda as seguintes questões:

# 1) Qual a hipótese nula a ser testada?
# 2) Qual o valor da estatística de teste?
# 3) Qual a conclusão do teste?

# dados vindo do enunciado
media_amostra = 485 # gramas
desvio_padrao_amostra = 20 # gramas
media = 500 # gramas
significancia = 0.05
confianca = 1 - significancia
n = 30

# calculando a probabilidade do limite superior e a partir dele, o Z
probabilidade = (0.5 + (confianca / 2))
z_alpha_2 = norm.ppf(probabilidade)
print(f"z_alpha_2: {z_alpha_2}")

# calculando o Z (fórmula nova para os testes)
z = (media_amostra - media) / (desvio_padrao_amostra / np.sqrt(n))
print(f"z: {z}")

p_valor = 2 * (1 - norm.cdf(abs(z)))
print(f"p_valor: {p_valor}")

# fazendo os critérios do Bicaudal (tanto menor igual quanto maior igual)
menor_ou_igual = z <= -z_alpha_2
maior_ou_igual = z >= z_alpha_2

deve_rejeitar_hipotese = menor_ou_igual or maior_ou_igual
print(f"Deve rejeitar a hipótese: {deve_rejeitar_hipotese}")