import pandas as pd
dados = pd.read_csv('src/parte1/dados.csv')

# Distribuição de Frequências para variáveis qualitativas (mas com Crosstab)

# cria os objetos para mudar as labels de acordo com o valor
sexos = {0: 'Masculino', 1: 'Feminino'}
cores = {0: 'Indígena', 2: 'Branca', 4: 'Preta', 6: 'Amarela', 8: 'Parda', 9: 'Sem declaração'}

# realiza o crosstab entre 2 variáveis qualitativas, o primeiro parâmetro da função crosstab é quem vai ficar na Linha e o segundo é a Coluna
frequencia = pd.crosstab(dados.Sexo, dados.Cor).rename(index = sexos).rename(columns = cores)
percentual = pd.crosstab(dados.Sexo, dados.Cor, normalize=True).rename(index = sexos).rename(columns = cores) * 100

print(frequencia)
print(percentual)


# Realizando um crosstab com função agregadora (no caso Média Aritmética da Renda de cada grupo):
frequenciaComMediaRenda = pd.crosstab(dados.Sexo, dados.Cor, aggfunc = 'mean', values = dados.Renda).rename(index = sexos).rename(columns = cores)
print(frequenciaComMediaRenda)