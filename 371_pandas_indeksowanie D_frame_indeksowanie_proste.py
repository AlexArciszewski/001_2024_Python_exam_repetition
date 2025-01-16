#Zadanie
# Wyświetl czas biegu oraz miasto dla 5 pierwszych osób za pomocą indeksowania prostego.



import pandas as pd
#Otwieram plik zawody

df = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\370_zawody.xlsx")

print(df.head())

print('\n')

print(df[['Czas biegu', 'Miasto']][:5])

#    Czas biegu    Miasto
# 0        2.11  Warszawa
# 1        2.07    Kraków
# 2        2.08    Kraków
# 3        2.32  Warszawa
# 4        2.22    Gdańsk