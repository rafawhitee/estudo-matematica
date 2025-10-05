import numpy as np

## Considere o seguinte sistema linear:
##  3x + 2y = 7
##  x - y = 2 
## Utilizando o método de eliminação de Gauss para resolver este sistema, qual é o par ordenado (x, y) que satisfaz ambas as equações?

A = np.array([[3, 2], [1, -1]])
b = np.array([7, 2])

# Resolvendo o sistema
solucao = np.linalg.solve(A, b)
print(f"Par ordenado (x, y): {solucao}")