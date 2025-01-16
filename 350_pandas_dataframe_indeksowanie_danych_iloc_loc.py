#Indeksowanie .loc() wyciaga dane na pdostawie etykiet9indeksów) wierszy i kolumn a iloc(0 na pdostawie numerow wierszy i kolumn. Dla wiersy zazwyczaj tożame wyciaganie  dla kolumn nie....

import pandas as pd
df = pd.read_excel('C:/Dane/2_ML_Projekty/003_programowanie_ML_zadanka_kurs_wprowadzenie/Moduł 2/Zbiory danych/pracownicy.xlsx')

print("Indeksowanie .loc() wyciaga dane na pdostawie etykiet(indeksów) wierszy i kolumn a iloc() na pdostawie numerow wierszy i kolumn")
print(df)
print("loc\n")
print(df.loc[2])

# Imię          Andrzej
# Nazwisko          Lis
# Wiek               32
# Staż               11
# Premia           0.02
# Zarobki         13000
# Płeć                M
# Miasto         Kraków
# Zawód       Kierownik
# Name: 2, dtype: object


print("\niloc\n")
print(df.iloc[2])

#Imię          Andrzej
#Nazwisko          Lis
#iek               32
#Staż               11
#Premia           0.02
#Zarobki         13000
#łeć                M
#Miasto         Kraków
#Zawód       Kierownik
#Name: 2, dtype: object

print("\ndf\n")

print(df[2:3])

#      Imię Nazwisko  Wiek  Staż  Premia  Zarobki Płeć  Miasto      Zawód
#2  Andrzej      Lis    32    11    0.02    13000    M  Kraków  Kierownik




