import numpy as np
import pandas as pd


class MathUtil():

    DEVIATION_COLUMN_NAME = 'Deviantion'
    DEVIATION_ABS_COLUMN_NAME = '|Deviantion|'
    MEAN_DEVIATION_ABS_COLUMN_NAME = '|Mean Deviantion|'

    # Regra de Sturges (k = 1 + 10/3 * log de N na base 10)
    @staticmethod
    def sturges(n):
        k = 1 + (10/3) * np.log10(n)
        return int(k.round(0))

    @staticmethod
    def getVariance(dataFrame, index):
        return dataFrame[index].pow(2)

    # Realiza o Desvio, o Desvio Absoluto e o Desvio Absoluto Médio
    @staticmethod
    def getDataFrameWithDeviantions(dataFrame, index):
        dataFrameToReturn = pd.DataFrame()  # create a new DataFrame
        # get values index (as dataframe)
        dataFrameWithOnlyIndexValues = dataFrame[[index]]
        # calc the mean of index values
        meanOfIndexValues = dataFrameWithOnlyIndexValues.mean()[0]
        # calc the Deviantion and put on dataFrameToReturn
        dataFrameToReturn[MathUtil.DEVIATION_COLUMN_NAME] = dataFrame[index] - \
            meanOfIndexValues
        # calculate the mean Deviantion and put on dataFrameToReturn
        dataFrameToReturn[MathUtil.DEVIATION_ABS_COLUMN_NAME] = dataFrameToReturn[MathUtil.DEVIATION_COLUMN_NAME].abs()
        # calculate the mean desvian absolut and put on dataFrameToReturn
        dataFrameToReturn[MathUtil.MEAN_DEVIATION_ABS_COLUMN_NAME] = dataFrameToReturn[MathUtil.DEVIATION_ABS_COLUMN_NAME].mean()
        return dataFrameToReturn
