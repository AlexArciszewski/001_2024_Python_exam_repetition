#Zadanie Zbuduj funkcję, która będzie przypisywała osobie wartość "Osoba wysoka" jeśli ma ponad 185 cm wzrostu,
# za to jeśli ma mniej niż 185 cm wzrostu funkcja zwróci wartość "Osoba nie jest wysoka".
# Za pomocą *apply* użyj funkcji na *df*.



import pandas as pd
import numpy as np

df = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\370_zawody.xlsx")


print(df.head())


def height(value):
    if value >= 185:
        return "Osoba wysoka"
    else:
        return  "Osoba nie jest wysoka"

df['Wzrost_kategoria'] = df['Wzrost'].apply(height)

print('\n')

print(df)

#        Imię  Rzut  Skok  ...    Miasto Wzrost       Wzrost_kategoria
#0   Karolina  8.03  3.13  ...  Warszawa    188           Osoba wysoka
#1    Mateusz  8.11  3.22  ...    Kraków    178  Osoba nie jest wysoka
#2    Paulina  7.44  2.98  ...    Kraków    182  Osoba nie jest wysoka
#3   Zdzisław  7.38  3.14  ...  Warszawa    188           Osoba wysoka
#4     Janusz  7.98  3.55  ...    Gdańsk    192           Osoba wysoka
#5       Ania  7.44  3.68  ...  Warszawa    190           Osoba wysoka
#6  Agnieszka  7.33  3.04  ...    Kraków    191           Osoba wysoka
#7    Natalia  7.23  2.74  ...  Warszawa    179  Osoba nie jest wysoka
#8      Kamil  6.59  2.94  ...    Gdańsk    178  Osoba nie jest wysoka
#9        Ewa  8.88  3.00  ...  Warszawa    182  Osoba nie jest wysoka

#[10 rows x 9 columns]