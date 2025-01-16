
#Zadanie 3. Ustaw imiona jako indeks naszej tabeli.


import pandas as pd
#Otwieram plik zawody

df = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\370_zawody.xlsx")

print(df.head())

print('\n')

print(df)

df.set_index('Imię', inplace=True)

print(df)

#Imię
#Karolina   8.03  3.13        2.11    Kobieta    Tak  Warszawa     188
#Mateusz    8.11  3.22        2.07  Mężczyzna    Tak    Kraków     178
#Paulina    7.44  2.98        2.08    Kobieta    Nie    Kraków     182
#dzisław   7.38  3.14        2.32  Mężczyzna    Nie  Warszawa     188
#anusz     7.98  3.55        2.22  Mężczyzna    Tak    Gdańsk     192
#nia       7.44  3.68        2.42    Kobieta    Nie  Warszawa     190
#gnieszka  7.33  3.04        2.52    Kobieta    Nie    Kraków     191
#Natalia    7.23  2.74        2.11    Kobieta    Tak  Warszawa     179
#Kamil      6.59  2.94        2.98  Mężczyzna    Nie    Gdańsk     178
#Ewa        8.88  3.00        2.04    Kobieta    Tak  Warszawa     182