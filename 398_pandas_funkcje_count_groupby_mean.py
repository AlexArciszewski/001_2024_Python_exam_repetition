#Zadanie
# Oblicz średni skok kobiet i mężczyzn.


import pandas as pd


df = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\370_zawody.xlsx")


print(df.groupby('Płeć')['Skok'].mean())


#Płeć
#Kobieta      3.0950
#Mężczyzna    3.2125
#Name: Skok, dtype: float64