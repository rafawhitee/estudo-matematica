import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('src/parte1/dados.csv')

# Separa a Renda em Quartis (4)
quantile = dados.Renda.quantile([0.25, 0.5, 0.75])
print("Quantile: ", str(quantile) + "\n")


# Separa a Renda em Decis (10)
decis = dados.Renda.quantile([i / 10 for i in range(1, 10)])
print("Decis: ", str(decis) + "\n")


# Separa a Renda em Percentis (100)
percentis = dados.Renda.quantile([i / 100 for i in range(1, 100)])
print("Percentis: ", str(percentis) + "\n")

# Histograma Acumulativo de Idade
ax = sns.distplot(dados.Idade, hist_kws = {'cumulative': True}, kde_kws = {'cumulative': True})
ax.figure.set_size_inches(14, 6)
plt.show()