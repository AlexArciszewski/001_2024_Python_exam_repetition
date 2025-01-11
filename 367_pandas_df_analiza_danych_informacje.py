# Zadanie
# Wyświetl podstawowe informacje o typach danych naszej tabeli danych.
# Wyświetl kształt tabeli danych (liczba wierszy i kolumn).


import pandas as pd
import numpy as np

df2 = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\363_pracadomowa.xlsx",
                   sheet_name='zarzad',
                   names=['Imię', 'Nazwisko', 'Wzrost', 'Kolor oczu'])

print(df2)

#     Imię  Nazwisko  Wzrost  Kolor oczu
#0  Szymon    Dajnik     164       Szare
#1  Patryk     Klops     188  Niebieskie
#2    Adam   Zielony     172     Zielone
#3  Kacper  Kowalski     188     Zielone


print('\n')

df2.info()


# Data columns (total 4 columns):
  #   Column      Non-Null Count  Dtype
#---  ------      --------------  -----
# 0   Imię        4 non-null      object
# 1   Nazwisko    4 non-null      object
# 2   Wzrost      4 non-null      int64
# 3   Kolor oczu  4 non-null      object
#dtypes: int64(1), object(3)
#memory usage: 260.0+ bytes

print(df2.shape)
#(4, 4)