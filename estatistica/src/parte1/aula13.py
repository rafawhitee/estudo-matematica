import pandas as pd

from utils.mock_util import MockUtil
from utils.math_util import MathUtil

dados = pd.read_csv('src/parte1/dados.csv')

# pega as notas dos Alunos
df = MockUtil.getDataFrameNotasAlunos()

# OBS: a implementação do Desvio Médio Absoluto eu deixei no MathUtil.py

# método criado no MathUtil
dataFrameFulano = MathUtil.getDataFrameWithDeviantions(df, 'Fulano')
dataFrameSicrano = MathUtil.getDataFrameWithDeviantions(df, 'Sicrano')

# faz os prints
print("Data Frame com os Devios de Fulano: \n" + str(dataFrameFulano) + "\n")
print("Data Frame com os Devios de Sicrano: \n" + str(dataFrameSicrano) + "\n")