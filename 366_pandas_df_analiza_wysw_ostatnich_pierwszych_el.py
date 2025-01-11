# Zadanie
# Wyświetl za pomocą odpowiedniej metody 2 pierwsze elementy tablicy.363_pracadomowa.xlsx




import pandas as pd
import numpy as np

df2 = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\363_pracadomowa.xlsx",
                   sheet_name='zarzad',
                   names=['Imię', 'Nazwisko', 'Wzrost', 'Kolor oczu'])

print(df2)


#     Imię  Nazwisko  Wzrost  Kolor oczu
# 0  Szymon    Dajnik     164       Szare
# 1  Patryk     Klops     188  Niebieskie
# 2    Adam   Zielony     172     Zielone
# 3  Kacper  Kowalski     188     Zielone
print('\n')


#2pierwsze elementy
print(df2.head(2))

#      Imię Nazwisko  Wzrost  Kolor oczu
# 0  Szymon   Dajnik     164       Szare
# 1  Patryk    Klops     188  Niebieskie

#3 ostatnie elementy
print(df2.tail(3))