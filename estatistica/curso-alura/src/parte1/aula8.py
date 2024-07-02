import pandas as pd
dados = pd.read_csv('src/parte1/dados.csv')

# o próprio pandas já tem função para realizar a mediana
rendaMediana = dados.Renda.median()
alturaMediana = dados.Altura.median()

print("Renda Mediana: ", str(rendaMediana))
print("\n")
print("Altura Mediana: ", str(alturaMediana))

# realiza a mediana, mas agrupada pelo sexo
rendaMedianaAgrupadaPeloSexo = dados.groupby(['Sexo'])['Renda'].median()
print("\n")
print("Renda Mediana agrupada pelo sexo: ", str(rendaMedianaAgrupadaPeloSexo))