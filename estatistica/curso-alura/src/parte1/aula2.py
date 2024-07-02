import pandas as pd
dados = pd.read_csv('src/parte1/dados.csv')

# Distribuição de Frequências para variáveis qualitativas

# ele faz o count de acordo com cada tipo de valores possíveis
frequencia = dados['Sexo'].value_counts()
percentual = dados['Sexo'].value_counts(normalize = True) * 100

# cria um DataFrame customizado do Pandas
dist_freq_qualitativas = pd.DataFrame({'Frequência': frequencia, 'Porcentagem (%)': percentual})

# muda as labels (0 --> Masculino e 1 --> Feminino)
dist_freq_qualitativas.rename(index = {0: 'Masculino', 1: 'Feminino'}, inplace = True)

print(dist_freq_qualitativas)