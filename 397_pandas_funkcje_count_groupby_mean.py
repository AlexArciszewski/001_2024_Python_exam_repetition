#Zadanie
# Wyznacz średnią czasu biegu mieszkańców poszczególnych miast.


import pandas as pd


df = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\370_zawody.xlsx")


print(df.head())



dfg = df.groupby('Miasto').count()
print(dfg)

#          Imię  Rzut  Skok  Czas biegu  Płeć  Zawody  Wzrost
#Miasto
#Gdańsk       2     2     2           2     2       2       2
#Kraków       3     3     3           3     3       3       3
#Warszawa     5     5     5           5     5       5       5

print(df.groupby('Miasto')['Czas biegu'].mean())


#Miasto
#Gdańsk      2.600000
#Kraków      2.223333
#Warszawa    2.200000
#Name: Czas biegu, dtype: float64
