from scipy.stats import binom

# Exercício: Suponha que a probabilidade de um casal ter filhos com olhos azuis seja de 22%.
# Em 50 famílias, com 3 crianças cada uma,
# quantas podemos esperar que tenham dois filhos com olhos azuis?

p = 0.22  # probabilidade de sucesso (olho azul)
k = 2  # total de filhos com olho azul que é desejado
n = 3  # total de crianças por família

probabilidade = binom.pmf(k, n, p)
print(
    f'Probabilidade de 2 crianças no total de 3 vir com olho azul: {probabilidade * 100}%')

numero_total_de_familias = 50
media_distribuicao_binomimal = numero_total_de_familias * probabilidade
print(f'Média da Distribuição Binomial: {media_distribuicao_binomimal}')
