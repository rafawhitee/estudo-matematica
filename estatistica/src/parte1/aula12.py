import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('src/parte1/dados.csv')

# Boxplot de Altura com a orientação horizontal
ax = sns.boxplot(x = 'Altura', data = dados, orient = 'h')
ax.figure.set_size_inches(12, 4)
plt.show()


# Boxplot de Renda com a orientação horizontal
ax = sns.boxplot(x = 'Renda', data = dados, orient = 'h')
ax.figure.set_size_inches(12, 4)
plt.show()


# Boxplot de Renda com query (ganhando menos de 10.000) e a orientação horizontal
ax = sns.boxplot(x = 'Renda', data = dados.query('Renda < 10000'), orient = 'h')
ax.figure.set_size_inches(12, 4)
plt.show()


# Boxplot de Altura no Eixo X e Sexo no Eixo Y com a orientação horizontal
ax2 = sns.boxplot(x = 'Altura', y = 'Sexo', data = dados, orient = 'h')
ax2.figure.set_size_inches(12, 4)
plt.show()