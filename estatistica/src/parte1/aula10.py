import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('dados.csv')

series = dados.query('Renda < 20000').Renda
ax = sns.distplot(series)
ax.figure.set_size_inches(12, 6)
plt.show()