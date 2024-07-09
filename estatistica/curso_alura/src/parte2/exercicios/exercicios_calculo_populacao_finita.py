from scipy.stats import norm


# Um fabricante de farinha verificou que, em uma amostra aleatória formada por 200 sacos de 25 kg de um lote formado por 2.000 sacos, 
# apresentou um desvio padrão amostral do peso igual a 480 g.
# Considerando um erro máximo associado à média populacional igual a 0,3 kg e um nível de confiança igual a 95%, 
# qual tamanho de amostra deveria ser selecionado para obtermos uma estimativa confiável do parâmetro populacional?

# população é finita, ele falou que são 2000 sacos
tamanho_populacao = 2000

# Erro inferencial
e = 0.3 # 0.3kg (300 gramas)

# tamanho da amostra
n = 200

# Desvio Padrão (deu o valor no enunciado)
desvio_padrao_amostral = 0.48 # 0.48kg (480 gramas)

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