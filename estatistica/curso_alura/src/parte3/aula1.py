import pandas as pd
import numpy as np
from scipy.stats import normaltest

dados = pd.read_csv('src/parte3/dados.csv')

significancia = 0.05 # 5%, logo é 95% de confiança


##
# 
#  TESTANDO COM A VARIÁVEL RENDA
#
##
stat_test_renda, p_valor_renda = normaltest(dados.Renda)
print(f"stat_test para dados.Renda: {stat_test_renda}")
print(f"p_valor para dados.Renda: {p_valor_renda}")

# se o p_valor for menor ou igual a significancia definida
# deve rejeitar a hipótese
# logo, a variável Renda não é uma distribuição normal
rejeita_hipotese_renda = p_valor_renda <= significancia
print(f"p_valor <= significancia para p_valor_renda: {rejeita_hipotese_renda}")


##
# 
#  TESTANDO COM A VARIÁVEL ALTURA
#
##
stat_test_altura, p_valor_altura = normaltest(dados.Altura)
print(f"\nstat_test para dados.Altura: {stat_test_altura}")
print(f"p_valor para dados.Altura: {p_valor_altura}")

# nesse caso abaixo, o valor é maior que a signifiância
# logo aceita a hipótese
# a variável altura é uma distribuição normal
rejeita_hipotese_altura = p_valor_altura <= significancia
print(f"p_valor <= significancia para p_valor_altura: {rejeita_hipotese_altura}")