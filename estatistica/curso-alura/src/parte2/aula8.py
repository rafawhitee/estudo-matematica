from scipy.stats import norm


# Estamos estudando o rendimento mensal dos chefes de domicílios no Brasil. 
# Nosso supervisor determinou que o erro máximo em relação a média seja de R$ 100,00. 
# Sabemos que o desvio padrão populacional deste grupo de trabalhadores é de R$ 3.323,39. 
# Para um nível de confiança de 95%, qual deve ser o tamanho da amostra de nosso estudo?

# Erro inferencial
e = 100 # ele já deu o erro inferente que é de no máximo 100 reais

# Desvio Padrão (deu o valor no enunciado)
sigma = 3323.39 # reais

# Nível de Significância (deu o valor no enunciado de 95% de confiança, logo é 5% de significância)
# representa a probabilidade de erro da estimativa
significania = 0.05 # 5%

# Nível de Confiança (1 - Significância)
# representa a probabilidade de acerto da estimativa
confianca = 1 - significania

# calcula a probabilidade até o limite superior
# como é uma distribuição normal, é simétrico
# então por isso divide a confianca em 2 (95% fica 47,5% para cada lado)
# então no lado direito tem 47,5% e do meio (média) até o menos infinito, sabe que é 50%, então fica 47,5% + 50.0% totalizando 97.5%
probabilidade_ate_limite_superior = (confianca / 2) + 0.5
Z = norm.ppf(probabilidade_ate_limite_superior)

n = (Z * (sigma / e)) ** 2
print(f"N: {int(n.round())}")