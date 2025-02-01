#Zadanie
#Użyj powyższej funkcji na kolumnie "Zawody" naszej tabeli danych. Sprawdź czy typ danych zmienił się na *bool*


import pandas as pd

df = pd.read_excel(r"C:\Dane\2_ML_Projekty\003_programowanie_ML_zadanka_kurs_wprowadzenie\Moduł 2\Zbiory danych\zledane.xlsx")

print(df.head())

print('\n')

def func(arg):
    if arg == 'Tak':
        return True
    else:
        return False

df.drop(0, inplace=True)
print(df)

df['Zawody'] = df['Zawody'].apply(func)

print(df['Zawody'].info())

#10 non-null     bool  TAK JEST BOOL