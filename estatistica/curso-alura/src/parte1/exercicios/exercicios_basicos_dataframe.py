import pandas as pd

data_frame = pd.DataFrame(data=[[1000, 110, 110, 10], [5000, 210, 160, 20], [16000, 350, 220, 45]],
                          index=['dragon', 'demon', 'orshabaal'],
                          columns=['life', 'base_attack', 'speed', 'shield'])

# acessando uma coluna e retornando em Series
print(f"\n data_frame['life'] (retorna em Series): {data_frame['life']} \n")

# acessando uma coluna e retornando em DataFrame
print(f"\n data_frame[['life']] (retorna em DataFrame): {data_frame[['life']]} \n")

# para acessar por index deve ser usar o .loc ou .iloc
print(f"data_frame.loc['dragon']]: {data_frame.loc[['dragon']]} \n")

# Frequência Absoluta (quantas vezes se repete)
print(
    f"Frequência Absoluta['life']: {str(data_frame['life'].value_counts())} \n")

# Frequência Relativa (quantas vezes se repete dividido pelo total)
print(
    f"Frequência Relativa['life']: {str(data_frame['life'].value_counts(normalize = True) * 100)} \n")
