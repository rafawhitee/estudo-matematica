import numpy as np
from scipy.stats import poisson

# DISTRIBUIÇÃO POISSON

# Exemplo: Um restaurante recebe em média, 20 pedidos por hora. 
#  Qual a chance de que, em determinada hora escolhido ao acaso,
# o restaurante receba apenas 15 pedido?

u = 20 # média que o problema fala (ele recebe em média 20 pedidos por hora)
k = 15 # k é o valor que desejado que desejamos calcular a probabilidade, no caso a probabilidade de receber apenas 15 em uma hora qualquer ao acaso

# fazendo o cálculo manualmente
probabilidade_manual = ((np.e ** (-u) ) * (u ** k)) / (np.math.factorial(k))
print(f"Probabilidade ao acaso escolher uma hora que receba 15 pedidos (cálculo manual): {probabilidade_manual * 100}%")

probabilidade_scipy = poisson.pmf(k, u)
print(f"Probabilidade ao acaso escolher uma hora que receba 15 pedidos (cálculo do scipy): {probabilidade_scipy * 100}%")