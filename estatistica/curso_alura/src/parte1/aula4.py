import pandas as pd

dados = pd.read_csv('src/parte1/dados.csv')

# Distribuição de Frequências para variáveis quantitativas (classes personalizadas)

# para criar classes personalizadas o pandas tem uma função própria
# vamos trabalhar com o campo Renda na época de 2015, que é baseado em salário mínimo (na época era R$ 788,00)

# começa em 0, depois 2 salários mínimos, 10 salários mínimos, 20 salários mínimos e o máximo dentro do CSV
classes = [0, 1576, 3152, 7880, 15760, dados.Renda.max()]

# labels para as classes de Renda, exemplo: E --> 0 até 1576 (0 até 2 salários mínimos)
labels = ['E', 'D', 'C', 'B', 'A']

# usa a função do pandas que efetua os limites e cria as classes personalizadas
# primeiro parâmetro (x) --> qual o dado que será realizado a classe personalizada
# segundo parâmetro (bins) --> os limites que o pandas deve ter para criar as classes personalizadas
# terceira parâmetro (labels) --> da o nome as classes personalizadas, seguindo o mesmo index do segundo parâmetro
# quarto parâmetro (include_lowest) --> por padrão, o pd.cut não inclui o menor valor, então deve passar esse para incluir os 0 (valor mínimo nesse caso)
series = pd.cut(x = dados.Renda, bins = classes, labels = labels, include_lowest = True)

# a partir das series criada, passa para a contagem e a porcentagem
frequencia = pd.value_counts(series)
percentual = pd.value_counts(series, normalize = True) * 100

# cria um DataFrame personalizada
dist_freq_quantitativas_personalizadas = pd.DataFrame({'Frequência': frequencia, 'Percentual (%):': percentual})
print(dist_freq_quantitativas_personalizadas)