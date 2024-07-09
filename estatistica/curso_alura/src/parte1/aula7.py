import pandas as pd
dados = pd.read_csv('src/parte1/dados.csv')

# o próprio pandas já tem função para realizar a média aritmética simples
rendaMedia = dados.Renda.mean()
alturaMedia = dados.Altura.mean()

print("Renda Media", str(rendaMedia))
print("Altura Media", str(alturaMedia))

# realiza a média, mas agrupada pelo sexo
rendaMediaAgrupadaPeloSexo = dados.groupby(['Sexo'])['Renda'].mean()
print("Renda Media agrupada pelo sexo", str(rendaMediaAgrupadaPeloSexo))