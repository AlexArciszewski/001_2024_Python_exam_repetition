#Zadanie Usuń pierwszy wiersz zawierający typy danych.

import pandas as pd

df = pd.read_excel(r"C:\Dane\2_ML_Projekty\003_programowanie_ML_zadanka_kurs_wprowadzenie\Moduł 2\Zbiory danych\zledane.xlsx")

print(df.head())
#print(df.tail())
#print(df.info())

#       Imię     Rzut     Skok Czas biegu       Płeć  Zawody    Miasto Wzrost
#0    String  Float64  Float64    Float64     String  String    String  Int64
#1  Karolina     8.03     3.13       2.11    Kobieta     Tak  Warszawa    188
#2   Mateusz     8.11     3.22       2.07  Mężczyzna     Tak    Kraków    178
#3   Paulina     7.44     2.98       2.08    Kobieta     Nie    Kraków    182
#4  Zdzisław     7.38     3.14       2.32  Mężczyzna     Nie  Warszawa    188

df.drop(0, inplace=True)
print('\n')
print(df)

#         Imię  Rzut  Skok Czas biegu       Płeć Zawody    Miasto Wzrost
#1    Karolina  8.03  3.13       2.11    Kobieta    Tak  Warszawa    188
#     Mateusz  8.11  3.22       2.07  Mężczyzna    Tak    Kraków    178
#3     Paulina  7.44  2.98       2.08    Kobieta    Nie    Kraków    182
#4    Zdzisław  7.38  3.14       2.32  Mężczyzna    Nie  Warszawa    188
#5      Janusz  7.98  3.55       2.22  Mężczyzna    Tak    Gdańsk    192
#6        Ania  7.44  3.68       2.42    Kobieta    Nie  Warszawa    190
#7   Agnieszka  7.33  3.04       2.52    Kobieta    Nie    Kraków    191
#8     Natalia  7.23  2.74       2.11    Kobieta    Tak  Warszawa    179
#9       Kamil  6.59  2.94       2.98  Mężczyzna    Nie    Gdańsk    178
#10        Ewa  8.88     3       2.04    Kobieta    Tak  Warszawa    182






