from scipy.stats import norm


# Em um lote de 10.000 latas de refrigerante foi realizada uma amostra aleatória simples de 100 latas e foi obtido o desvio padrão amostral do conteúdo 
# das latas igual a 12 ml. O fabricante estipula um erro máximo sobre a média populacional de apenas 5 ml. 
# Para garantir um nível de confiança de 95% qual o tamanho de amostra deve ser selecionado para este estudo?

# população é finita, ele falou que são 10.000 latas
tamanho_populacao = 10000

# Erro inferencial
e = 5 # 5 ml

# tamanho da amostra
n = 100

# Desvio Padrão (deu o valor no enunciado)
desvio_padrao_amostral = 12 # 12 ml

# Nível de Significância
significania = 0.05 # 5%

# Nível de Confiança (1 - Significância)
confianca = 1 - significania

# calcula a probabilidade até o limite superior
# como é uma distribuição normal, é simétrico
# então por isso divide a confianca em 2 (95% fica 47,5% para cada lado)
# então no lado direito tem 47,5% e do meio (média) até o menos infinito, sabe que é 50%, então fica 47,5% + 50.0% totalizando 97.5%
probabilidade_ate_limite_superior = (confianca / 2) + 0.5
Z = norm.ppf(probabilidade_ate_limite_superior)

n1 = (Z ** 2) * (desvio_padrao_amostral ** 2) * tamanho_populacao
n2 = (Z ** 2) * (desvio_padrao_amostral ** 2) + ( (e ** 2) * (tamanho_populacao - 1))
n = n1 / n2
print(f"N: {int(n.round())}")