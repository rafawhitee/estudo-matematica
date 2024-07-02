from scipy.special import comb
from scipy.stats import binom

# DISTRIBUIÇÃO BINOMIAL

# Exemplo 1 --> Mega Sena (fazendo o jogo de 6 números num total de 60 disponível)
combinacoesMegaSena = comb(60, 6)
probabilidadeDeGanhar = 1 / combinacoesMegaSena

print("Combinações da Mega Sena: " + str(combinacoesMegaSena))
print("Probabilidade de Ganhar na Mega Sena: %0.25f" % probabilidadeDeGanhar)


# Exemplo 2:
# Em um concurso para preencher uma vaga de Cientista de Dados temos um total de 10 questões de múltipla escolha
# com 3 alternativas possíveis em cada questão. Cada questão tem o mesmo valor. Suponha que um candidato resolva se aventurar
# sem ter estudado absolutamente nada. Ele resolve fazer a prova de olhos fechados e chutar todas as respostas.
# Assumindo que a prova vale 10 pontos e a nota de corte seja 5, obtenha a probabilidade deste candidato acertar 5 questões
# e também a probabilidade deste candidato passar para a próxima etapa do processo seletivo

# Resolvendo a primeira parte (acertar 5 questões)

n = 10  # total de questões
numeroDeAlternativasPorQuestao = 3
p = 1 / numeroDeAlternativasPorQuestao  # probabilidade de acertar
q = 1 - p  # probabilidade de errar
k = 5  # total de eventos para ocorrer o sucesso (no caso acertar 5 questões)

# manualmente
probabilidadeParte1 = (comb(n, k)) * (p ** k) * (q ** (n - k))
print("Probabilidade da parte 1 é igual a: %0.8f" % probabilidadeParte1)

# com a biblioteca Scipy
probabilidadeParte1Nativa = binom.pmf(k, n, p)
print("Probabilidade da parte 1 é igual a: %0.8f (nativa do Scipy)" %
      probabilidadeParte1Nativa)


# Resolvendo a segunda parte (passando para a próxima fase, no caso tem que acerter no mínimo 5 questões)

# você consegue passar uma lista de valores de sucesso para ele
# ele retorna uma lista de probabilidade para cada
# por exemplo o index 0 é o 5, no caso, 5 questões acertadas, no retorno index 0 ele retorna a probabilidade de acertar 5 questões
# por exemplo 2 o index 5 é o 10, no caso, 10 questões acertadas (todas), no retorno index 5 ele retorna a probabilidade de acertar todas as 10 questões
probabilidadeParte2 = binom.pmf([5, 6, 7, 8, 9, 10], n, p).sum()
print("Probabilidade da parte 2 é igual a: %0.8f" % probabilidadeParte2)

# fazendo pelo caminho ao contrário (destrutivo)

# o CDF é acumulativo até o número em questão, no caso eu passei o valor 4, então ele faz o seguinte:
# probabilidade de acertar nenhuma questão das 10
# probabilidade de acertar 1 questão das 10
# probabilidade de acertar 2 questões das 10
# probabilidade de acertar 3 questões das 10
# probabilidade de acertar 4 questões das 10
probabilidadeDeAcertarAteQuatroQuestoes = binom.cdf(4, n, p)
print("Probabilidade de acertar até 4 é igual a: %0.8f" % probabilidadeDeAcertarAteQuatroQuestoes)

# então para calcular o da parte 2, basta fazer 1 - o binom acima
probabilidadeParte2MetodoDestrutivo = 1 - probabilidadeDeAcertarAteQuatroQuestoes

# obs o binom.sf já faz essa conta do 1 - binom.cdf(4, n, p)
print("Probabilidade da parte 2 é igual a (método destrutivo): %0.8f" % probabilidadeParte2MetodoDestrutivo)