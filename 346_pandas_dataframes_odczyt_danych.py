import pandas as pd

df_1 = pd.read_excel("C:/Dane/2_ML_Projekty/003_programowanie_ML_zadanka_kurs_wprowadzenie/001_dane.xlsx")
print(df_1)

# Otwieranie kolejnego arkusza w tym samym pliku excel
df_2 = pd.read_excel("C:/Dane/2_ML_Projekty/003_programowanie_ML_zadanka_kurs_wprowadzenie/001_dane.xlsx", sheet_name='kolejny arkusz')
print(df_2)

# zdefiniowanie nazw kolumn gdy chcemy cos np zmienic w nazwach kolumn
# zmieniamy kolumny how_many na some_number w names wypisujemy kolejno nazwy  kolumn:
# names = ['NaN' , 'NaN', 'NaNlp', 'dzien', 'data', 'day', 'example', 'some_number', 'random_stuff']

df_2 = pd.read_excel("C:/Dane/2_ML_Projekty/003_programowanie_ML_zadanka_kurs_wprowadzenie/001_dane.xlsx", sheet_name='kolejny arkusz',
                    names = ['NaN' , 'NaN', 'NaNlp', 'dzien', 'data', 'day', 'example', 'some_number', 'random_stuff'])
print(df_2)


# Otwarcie pliku cvs iris
import pandas as pd
df_4 = pd.read_csv("C:/Dane/2_ML_Projekty/003_programowanie_ML_zadanka_kurs_wprowadzenie/002_iris.csv")
print(df_4)

# Eksport danych
df_4.to_excel("C:/Dane/2_ML_Projekty/003_programowanie_ML_zadanka_kurs_wprowadzenie/002_iris.xlsx", sheet_name ='kwiatki')