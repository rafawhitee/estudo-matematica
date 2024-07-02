import pandas as pd
dados = pd.read_csv('src/parte1/dados.csv')

print(dados.Idade.unique())

# Qualitativas Ordinais --> são variáveis que podem ser ordenadas a nível de análise (uma melhor que a outra por exemplo)
qualitativasOrdinais = sorted(dados['Anos de Estudo'].unique())
print("qualitativasOrdinais (Anos de Estudo) --> ", str(qualitativasOrdinais))


# Qualitativas Nominais --> são variáveis que NÃO podem ser ordenadas a nível de análise
qualitativasNominaisUF = sorted(dados['UF'].unique())
print("qualitativasNominais (UF) --> ", str(qualitativasNominaisUF))

qualitativasNominaisCor = sorted(dados['Cor'].unique())
print("qualitativasNominais (Cor) --> ", str(qualitativasNominaisCor))


# Quantitativas Discretas (que são contadas e NÃO SÃO pontos flutuantes)
print("Quantitativas Discretas --> De %s até %s anos" % (dados.Idade.min(), dados.Idade.max()))


# Quantitativas Contínuas (que são contadas e SÃO pontos flutuantes)
print("Quantitativas Contínuas --> De %s até %s metros" % (dados.Altura.min(), dados.Altura.max()))