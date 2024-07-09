from scipy.stats import norm

# O valor do gasto médio dos clientes de uma loja de conveniência é de R$ 45,50. 
# Assumindo que o desvio padrão dos gastos é igual a R$ 15,00, qual deve ser o tamanho da amostra para estimarmos 
# a média populacional com um nível de significância de 10%?
# Considere que o erro máximo aceitável seja de 10%.

# média populacional
media = 45.50

# Erro inferencial (em porcentagem)
# como ele falou em porcentagem e deu a média, e feito os 10% da média
e = media * 0.1 # 10%, em relação a média

# Desvio Padrão (deu o valor no enunciado)
desvio_padrao = 15 # reais

# Nível de Significância
significania = 0.10 # 10%

# Nível de Confiança (1 - Significância)
confianca = 1 - significania

# calcula a probabilidade até o limite superior
probabilidade_ate_limite_superior = (confianca / 2) + 0.5
Z = norm.ppf(probabilidade_ate_limite_superior)

n = (Z * (desvio_padrao / e)) ** 2
print(f"N: {int(n.round())}")