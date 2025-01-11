# Zadanie
# Zaimportuj drugi arkusz "zarzad" z pliku *pracadomowa.xlsx*. Przy importowaniu podaj nazwy kolumn "Imię, Nazwisko,
# Wzrost, Kolor oczu". Wyświetl tą tabelę.


import pandas as pd
import numpy as np

#df = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\363_pracadomowa.xlsx",
                   #sheet_name='zarzad')

#print(df)

#    Nazwa1    Nazwa2  Nazwa3      Nazwa4
# 0  Szymon    Dajnik     164       Szare
# 1  Patryk     Klops     188  Niebieskie
# 2    Adam   Zielony     172     Zielone
# 3  Kacper  Kowalski     188     Zielone


df2 = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\363_pracadomowa.xlsx",
                   sheet_name='zarzad',
                   names=['Imię', 'Nazwisko', 'Wzrost', 'Kolor oczu'])

print(df2)


#     Imię  Nazwisko  Wzrost  Kolor oczu
# 0  Szymon    Dajnik     164       Szare
# 1  Patryk     Klops     188  Niebieskie
# 2    Adam   Zielony     172     Zielone
# 3  Kacper  Kowalski     188     Zielone