from scipy.stats import norm

# Utilizando a tabela padronizada, ou o ferramental disponibilizado pelo Python, encontre a área sob a curva normal para os valores de Z abaixo:
# A) Z < 1,96
# B) Z > 2,15
# C) Z < -0,78
# D) Z > 0,59


probabilidade_caso_a = norm.cdf(1.96)
print(f"Probabilidade do Primeiro Caso (Z < 1,96): {probabilidade_caso_a * 100}%")

probabilidade_caso_b = 1 - norm.cdf(2.15)
print(f"Probabilidade do Segundo Caso (Z > 2,15): {probabilidade_caso_b * 100}%")

probabilidade_caso_c = 1 - norm.cdf(-0.78)
print(f"Probabilidade do Terceiro Caso (Z < -0,78): {probabilidade_caso_c * 100}%")

probabilidade_caso_d = 1 - norm.cdf(0.59)
print(f"Probabilidade do Quarto Caso (Z > 0,59): {probabilidade_caso_d * 100}%")