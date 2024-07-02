import pandas as pd

dados = pd.read_csv('src/parte2/dados.csv')

# calcula a média geral a partir de todos os dados
renda_media = dados.Renda.mean()
print(f"Renda Média Geral: R$ {renda_media}")

# pega a porcentagem do sexo masculino (index 0) e do sexo feminino (index 1)
df_sexo_values_counts = dados.Sexo.value_counts(normalize=1)
porcentagem_masculino = df_sexo_values_counts[0]
porcentagem_feminino = df_sexo_values_counts[1]

print(f"Porcentagem de homens: {porcentagem_masculino * 100}%")
print(f"Porcentagem de mulheres: {porcentagem_feminino * 100}%")

# seed para criar as amostras simples
random_state = 101

# cria as amostras simples especificando a quantidade de linhas e o seed

# Amostra 1 com 100 linhas
quantidade_linhas_amostra_1 = 100
amostra_1 = dados.sample(n=quantidade_linhas_amostra_1,
                         random_state=random_state)

renda_media_amostra_1 = amostra_1.Renda.mean()
print(f"\nRenda Média da Amostra 1 com {quantidade_linhas_amostra_1} linhas: R$ {renda_media_amostra_1}")

df_sexo_values_counts_amostra_1 = amostra_1.Sexo.value_counts(normalize=1)
porcentagem_masculino_amostra_1 = df_sexo_values_counts_amostra_1[0]
porcentagem_feminino_amostra_1 = df_sexo_values_counts_amostra_1[1]

print(f"Porcentagem de homens (Amostra 1): {porcentagem_masculino_amostra_1 * 100}%")
print(f"Porcentagem de mulheres (Amostra 1): {porcentagem_feminino_amostra_1 * 100}%")

# Amostra 2 com 1000 linhas
quantidade_linhas_amostra_2 = 1000
amostra_2 = dados.sample(n=quantidade_linhas_amostra_2,
                         random_state=random_state)

renda_media_amostra_2 = amostra_2.Renda.mean()
print(f"\nRenda Média da Amostra 2 com {quantidade_linhas_amostra_2} linhas: R$ {renda_media_amostra_2}")

df_sexo_values_counts_amostra_2 = amostra_2.Sexo.value_counts(normalize=1)
porcentagem_masculino_amostra_2 = df_sexo_values_counts_amostra_2[0]
porcentagem_feminino_amostra_2 = df_sexo_values_counts_amostra_2[1]

print(f"Porcentagem de homens (Amostra 2): {porcentagem_masculino_amostra_2 * 100}%")
print(f"Porcentagem de mulheres (Amostra 2): {porcentagem_feminino_amostra_2 * 100}%")


# Observação:

# Existe mais 2 tipos de Amostragem: Estratificada e por Conglomerada

# Estratificada --> faz alguma restrição ou divisão de uma população para a partir dessa divisão fazer uma amostragem simples.
# Exemplo de Estratificada --> separar uma população por Classe de Renda (regra de sturges por exemplo), e a partir de cada amostras dessas classes, fazer uma amostragem simples.


# Conglomerada --> ela parece um pouco com a estratificada, mas a principal diferença é que a estratificada é homogênea, pegam valores próximos de algum atributo. 
# Aqui a divisão é feita por localização geográfica.