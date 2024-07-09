import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dados = pd.read_csv('src/parte2/dados.csv')

# O Teorema do Limite Central afirma que, com o aumento do tamanho da amostra, 
# a distribuição das médias amostrais se aproxima de uma distribuição normal com média igual à média da população e 
# desvio padrão igual ao desvio padrão da variável original dividido pela raiz quadrada do tamanho da amostra. 
# Este fato é assegurado para n maior ou igual a 30.


# Entendendo o Teorema do Limite Central

# cria um dataframe vazio
amostras = pd.DataFrame()

# vamos fazer 1500 amostras, e para cada amostra, ele irá pegar 2000 linhas aleatoriamente do dados2.csv
n = 2000
total_de_amostras = 1500

# monta a tabela de 1500x2000 (Colunas x Linhas)
for i in range(total_de_amostras):
    # para cada iteração, faz uma amostragem simples da variável N (no caso 2000), 
    # somente pegando a Idade, ignroando as outras colunas do dataframe original
    _ = dados.Idade.sample(n)
    _.index = range(0, len(_))
    # concatena no dataframe criado antes do for
    amostras['Amostras_' + str(i)] = _


# 1 parte --> com o aumento do tamanho da amostra, a distribuição das médias amostrais se aproxima de uma distribuição normal
# repare no histograma, que se aproxima e muito de uma Distribuição Normal
amostras.mean().hist()
plt.show()


# 2 parte --> com média igual (da amostra) à média da população
print(f"Idade Média de todos os dados: {dados.Idade.mean()}")
print(f"Média de todas as amostragens: {amostras.mean().mean()}")


# 3 parte --> desvio padrão igual ao desvio padrão da variável original dividido pela raiz quadrada do tamanho da amostra
desvio_padrao_das_amostras = amostras.mean().std()
desvio_padrao_geral_na_formula = dados.Idade.std() / np.sqrt(n)
print(f"Desvio Padrão das amostras: {desvio_padrao_das_amostras}")
print(f"Desvio Padrão de todos os dados utilizando a fórmula: {desvio_padrao_geral_na_formula}")


# Resumindo:
# Quanto maior o N, mais ela fica próxima de (sendo n >= 30):
# 1) Distribuição Normal
# 2) Média da Amostra muito próxima da média da população
# 3) Desvio padrão da amostra muito próximo do desvio padrão da população