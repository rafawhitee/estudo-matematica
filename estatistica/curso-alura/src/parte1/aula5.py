import pandas as pd
from utils.math_util import MathUtil

dados = pd.read_csv('src/parte1/dados.csv')

# Distribuição de Frequências para VARIÁVEIS QUANTITATIVAS (classes de amplitude fixa com Regra de Sturges)

# pega quantos dados tem no CSV
n = dados.shape[0]

# aplica a fórmula da Regra de Sturges (k = 1 + 10/3 * log de N na base 10)
# para saber quantas classes deverão ser criadas (com amplitude fixa)
k = MathUtil.sturges(n)

cutted = pd.cut(x = dados.Renda, bins = k, include_lowest = True)
frequencia = pd.value_counts(cutted, sort = False)
percentual = pd.value_counts(cutted, sort = False, normalize = True) * 100

dist_freq_quantitativas_amplitude_fixa = pd.DataFrame({'Frequência': frequencia, 'Percentual (%):': percentual})

print(dist_freq_quantitativas_amplitude_fixa)