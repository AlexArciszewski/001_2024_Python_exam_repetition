#Zadanie Zdefiniuj funkcję, która zsumuje wynik "Rzut" oraz "Skok" i zwróci wartość "Dobry wynik" jeśli ich suma będzie
# większa od 11,5, za to jeśli będzie mniejsza lub równa to ma zwrócić "Zły wynik".
#WSKAZÓWKA: Do funkcji podaj tylko jeden argument, który będzie listą dwóch argumentów - Rzut oraz Skok.



import pandas as pd
import numpy as np

df = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\370_zawody.xlsx")


print(df.head())


#row to pojedynczy wiersz DF
def score(row):
    sum = row['Rzut'] + row['Skok']

    if sum >= 11.5:
        return "Dobry wynik"
    else:
        return "Zły wynik"

df['Wynik'] = df.apply(score, axis=1)
#df['Wynik'] = df.apply(lambda row: score(row), axis=1)

print(df)


#        Imię  Rzut  Skok  Czas biegu  ... Zawody    Miasto Wzrost        Wynik
#0   Karolina  8.03  3.13        2.11  ...    Tak  Warszawa    188    Zły wynik
#1    Mateusz  8.11  3.22        2.07  ...    Tak    Kraków    178    Zły wynik
#2    Paulina  7.44  2.98        2.08  ...    Nie    Kraków    182    Zły wynik
#3   Zdzisław  7.38  3.14        2.32  ...    Nie  Warszawa    188    Zły wynik
#4     Janusz  7.98  3.55        2.22  ...    Tak    Gdańsk    192  Dobry wynik
#5       Ania  7.44  3.68        2.42  ...    Nie  Warszawa    190    Zły wynik
#6  Agnieszka  7.33  3.04        2.52  ...    Nie    Kraków    191    Zły wynik
#7    Natalia  7.23  2.74        2.11  ...    Tak  Warszawa    179    Zły wynik
#8      Kamil  6.59  2.94        2.98  ...    Nie    Gdańsk    178    Zły wynik
#9        Ewa  8.88  3.00        2.04  ...    Tak  Warszawa    182  Dobry wynik