import pandas as pd
dados = pd.read_csv('src/parte1/dados.csv')

# o próprio pandas já tem função para realizar a Moda
rendaModa = dados.Renda.mode()
alturaModa = dados.Altura.mode()

rendaMedianaAgrupadaPeloSexo = dados.groupby(['Sexo']).median()
print("Renda Moda: ", str(rendaModa))
print("\n")
print("Altura Moda: ", str(alturaModa))

rendaModaAgrupadaPeloSexo = dados.groupby(['Sexo']).Renda.median()
print("\n")
print("Renda Moda agrupada pelo sexo: ", str(rendaModaAgrupadaPeloSexo))