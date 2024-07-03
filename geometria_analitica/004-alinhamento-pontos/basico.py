from utils import *

# Cria os 3 pontos
A = (2, 5)
B = (3, 9)
C = (4, 11)

coef_angular_ab = coeficiente_angular(A, B)
coef_angular_bc = coeficiente_angular(B, C)

print(f"São Colineares (alinhados): {coef_angular_ab == coef_angular_bc}")