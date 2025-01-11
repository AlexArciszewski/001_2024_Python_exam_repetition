#Sprawdź ile w zbiorze danych znajduje się osób o każdym kolorze oczu. Posortuj wyniki malejąco


import pandas as pd
import numpy as np

df = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\363_pracadomowa.xlsx",
                   sheet_name='zarzad',
                   names=['Imię', 'Nazwisko', 'Wzrost', 'Kolor oczu'])

print(df)

#     Imię  Nazwisko  Wzrost  Kolor oczu
# 0  Szymon    Dajnik     164       Szare
# 1  Patryk     Klops     188  Niebieskie
# 2    Adam   Zielony     172     Zielone
# 3  Kacper  Kowalski     188     Zielone


print('\n')
print(df.sort_values(by='Kolor oczu', ascending=False))

#    Imię  Nazwisko  Wzrost  Kolor oczu
#2    Adam   Zielony     172     Zielone
#3  Kacper  Kowalski     188     Zielone
#0  Szymon    Dajnik     164       Szare
#1  Patryk     Klops     188  Niebieskie
print('\n')
print(df['Kolor oczu'].value_counts().sort_values(ascending=False))

#Kolor oczu
#Zielone       2
#Szare         1
#Niebieskie    1
#Name: count, dtype: int64