# Zadanie 2. Wyświetl Imię oraz Wzrost trzech ostatnich osób.
import pandas as pd
#Otwieram plik zawody

df = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\370_zawody.xlsx")

print(df.head())

print('\n')

print(df)

print('\n')

print(df[['Imię', 'Wzrost']][-3:])