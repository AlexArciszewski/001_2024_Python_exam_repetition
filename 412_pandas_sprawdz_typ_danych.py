#Zadanie 1. Sprawdź typy danych poszczególnych kolumn w *DataFrame*

import pandas as pd

df = pd.read_excel(r"C:\Dane\2_ML_Projekty\003_programowanie_ML_zadanka_kurs_wprowadzenie\Moduł 2\Zbiory danych\zledane.xlsx")

print(df.head())
print(df.tail())
print(df.info())

#dtypes: object(8)
#memory usage: 836.0+ bytes
#None




