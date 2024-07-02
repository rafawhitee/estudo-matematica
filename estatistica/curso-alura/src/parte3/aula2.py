import pandas as pd
import numpy as np
from scipy.stats import norm
from statsmodels.stats.weightstats import ztest

# A empresa **Suco Bom** produz **sucos de frutas em embalagens de 500 ml**. Seu processo de produção é quase todo automatizado e as embalagens de sucos 
# são preenchidas por uma máquina que às vezes apresenta um certo desajuste, levando a erros no preenchimento das embalagens para mais ou menos conteúdo. 
# Quando o volume médio cai abaixo de 500 ml, a empresa se preocupa em perder vendas e ter problemas com os orgãos fiscalizadores. 
# Quando o volume passa de 500 ml, a empresa começa a se preocupar com prejuízos no processo de produção.

# O setor de controle de qualidade da empresa **Suco Bom** extrai, periodicamente, **amostras de 50 embalagens** para monitorar o processo de produção.
# Para cada amostra, é realizado um **teste de hipóteses** para avaliar se o maquinário se desajustou. 
# A equipe de controle de qualidade assume um **nível de significância de 5%**.

# Suponha agora que uma **amostra de 50 embalagens** foi selecionada e que a **média amostral observada foi de 503,24 ml**. 
# **Esse valor de média amostral é suficientemente maior que 500 ml para nos fazer rejeitar a hipótese de que a média do processo é de 500 ml 
# ao nível de significância de 5%?**

# simulando uma amostra
amostra = [509, 505, 495, 510, 496, 509, 497, 502, 503, 505, 
           501, 505, 510, 505, 504, 497, 506, 506, 508, 505, 
           497, 504, 500, 498, 506, 496, 508, 497, 503, 501, 
           503, 506, 499, 498, 509, 507, 503, 499, 509, 495, 
           502, 505, 504, 509, 508, 501, 505, 497, 508, 507]
amostra = pd.DataFrame(amostra, columns=['Amostra'])

media_amostra = amostra.mean()[0]
desvio_padrao_amostra = amostra.std()[0]

# dados vindo do enunciado
media = 500
significancia = 0.05
confianca = 1 - significancia
n = 50

# calculando a probabilidade do limite superior e a partir dele, o Z
probabilidade = (0.5 + (confianca / 2))
z_alpha_2 = norm.ppf(probabilidade)

# calculando o Z (fórmula nova para os testes)
z = (media_amostra - media) / (desvio_padrao_amostra / np.sqrt(n))

# fazendo os critérios do Bicaudal (tanto menor igual quanto maior igual)
menor_ou_igual = z <= -z_alpha_2
maior_ou_igual = z >= z_alpha_2

deve_rejeitar_hipotese = menor_ou_igual or maior_ou_igual
print(f"Deve rejeitar a hipótese: {deve_rejeitar_hipotese}")


# Calculando o P Valor com o ZTEST
output_ztest = ztest(x1 = amostra, value = media)
print(f"Ztest output: {output_ztest}")