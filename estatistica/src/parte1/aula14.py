from utils.mock_util import MockUtil

# pega as notas dos Alunos
dataFrame = MockUtil.getDataFrameNotasAlunos()

# método nativo para calcular a variância
variancia = dataFrame['Fulano'].var()

print("Variância: " + str(variancia))
