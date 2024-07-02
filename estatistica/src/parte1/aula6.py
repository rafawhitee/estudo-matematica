import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('src/parte1/dados.csv')

# utilizando o seaborn
ax = sns.histplot(dados.Altura, kde = False)
ax.figure.set_size_inches(12, 6)
ax.set_title('Distribuição de Frequências - Altura (Seaborn)', fontsize = 18)
ax.set_xlabel('Metros', fontsize = 14)
plt.show()

# utilizando o próprio pandas
dados.Altura.hist(bins = 50, figsize = (12,6))
plt.show()