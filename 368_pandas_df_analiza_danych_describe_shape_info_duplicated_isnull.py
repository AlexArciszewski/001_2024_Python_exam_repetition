# Zadanie
# Wyświetl podstawowe informacje o typach danych naszej tabeli danych. df.info()
# Wyświetl kształt tabeli danych (liczba wierszy i kolumn). df.shape
# Sprawdz czy są puste rekordy df.isnull()
# Sprawdź dupliaty df.duplicated()


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
#     Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
# 0   Imię        4 non-null      object
# 1   Nazwisko    4 non-null      object
# 2   Wzrost      4 non-null      int64
# 3   Kolor oczu  4 non-null      object
# dtypes: int64(1), object(3)
# memory usage: 260.0+ bytes

print(df2.shape)
#(4, 4)

print('\n')
print(df2.describe())


#       Wzrost
# count     4.0
# mean    178.0
# std      12.0
# min     164.0
# 25%     170.0
# 50%     180.0
# 75%     188.0
# max     188.0


print(df2.isnull())

#    Imię  Nazwisko  Wzrost  Kolor oczu
# 0  False     False   False       False
# 1  False     False   False       False
# 2  False     False   False       False
# 3  False     False   False       False


print(df2.duplicated())

# 0    False
# 1    False
# 2    False
# 3    False
# dtype: bool

print(df2.isnull().sum())
# Imię          0
# Nazwisko      0
# Wzrost        0
# Kolor oczu    0
# dtype: int64
