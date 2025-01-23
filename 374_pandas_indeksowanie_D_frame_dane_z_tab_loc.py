#znajdź dane dotyczące kamila wykorzystując loc
import pandas as pd
#Otwieram plik zawody

df = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\370_zawody.xlsx")

print(df.head())

print('\n')

print(df)

#Zmiana indeksu na imię

df = df.set_index('Imię')

#dopiero loc
print(df.loc['Kamil'])