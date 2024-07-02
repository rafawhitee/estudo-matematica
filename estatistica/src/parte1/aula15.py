import numpy as np

from utils.mock_util import MockUtil

# pega as notas dos Alunos
dataFrame = MockUtil.getDataFrameNotasAlunos()

# manualmente (é a raiz quadrada da variância)
variancia = dataFrame['Fulano'].var()
desvioPadraoManualmente = np.sqrt(variancia)

# nativo do Pandas
desvioPadraoPandas = dataFrame['Fulano'].std()

print("Desvio Padrao Manualmente: " + str(desvioPadraoManualmente))
print("Desvio Padrao Pandas: " + str(desvioPadraoPandas))