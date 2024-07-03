from utils import equacao_reduzida

A = (5,2)
B = (7,5)
equacao_reduzida_AB = equacao_reduzida(A, B)
print(f"Equação reduzida de {A} e {B} --> {equacao_reduzida_AB}")

C = (6, 12)
D = (4, 18)
equacao_reduzida_CD = equacao_reduzida(C, D)
print(f"Equação reduzida de {C} e {D} --> {equacao_reduzida_CD}")