#Zadanie Pogrupuj powyższy zbiór danych względem Płci oraz Miasta. Dla otrzymanej tabeli znajdź przeciętny wzrost osób.

import pandas as pd


df = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\370_zawody.xlsx")

print(df)
print(df.groupby(['Płeć', 'Miasto']).agg({'Wzrost': 'mean'}))

#                    Wzrost
#Płeć      Miasto
#Kobieta   Kraków    186.50
#          Warszawa  184.75
#Mężczyzna Gdańsk    185.00
#          Kraków    178.00
#          Warszawa  188.00