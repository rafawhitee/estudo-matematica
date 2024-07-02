from scipy.stats import binom

# Exercício 3 (Gincana):
# Uma cidade do interior realiza todos os anos uma gincana para arrecadar fundos para o hospital da cidade.
# Na última gincana se sabe que a proporção do sexo feminino foi de 60%. O total de equipes, com 12 integrantes, inscritas na gincana é de 30.
# Com as informações acima responda: Quantas equipes deverão ser formadas por 8 mulheres?

# primeiro vamos calcular a probabilidade de montar 1 equipe primeiro
# sabe que a chance de escolher uma mulher é de 60% (homem é 40%), pois a proporção é 60%
p = 0.6 # probabilidade de escolher mulher
k = 8 # quantas mulheres nessa equipe deve ter, no caso ele quer 8 mulheres no grupo de 12 (os outros 4 serão homens)
n = 12 # total de pessoas na equipe

probabilidade = binom.pmf(k, n, p)
print(f'probabilidade de uma equipe ter 8 mulheres e 4 homens: {probabilidade * 100}%')

# agora que calculamos a probabilidade de montar uma única equipe com 8 mulheres e 4 homens
# vamos calcular a média com essa probabilidade com as 30 equipes (são 30 no total da gincana)
# Média da Distribuição Binomimal
total_equipes = 30
media_distribuicao_binomimal = total_equipes * probabilidade
print(f'Média da Distribuição Binomimal para as 30 equipes, a média é: {media_distribuicao_binomimal}')