#indeksowanie danych


import pandas as pd
df_4 = pd.read_csv("C:/Dane/2_ML_Projekty/003_programowanie_ML_zadanka_kurs_wprowadzenie/002_iris.csv")
print(df_4)

print("Indeksowanie proste wiersze 0 i 1 oraz nagółwek")
print(df_4[:2])

#[149 rows x 5 columns]
#   5.1  3.5  1.4  0.2  Iris-setosa
#0  4.9  3.0  1.4  0.2  Iris-setosa
#1  4.7  3.2  1.3  0.2  Iris-setosa


print("Indeksowanie proste wiersze 1,2,3  oraz nagółwek")
print(df_4[1:4])

#   5.1  3.5  1.4  0.2  Iris-setosa
#1  4.7  3.2  1.3  0.2  Iris-setosa
#2  4.6  3.1  1.5  0.2  Iris-setosa
#3  5.0  3.6  1.4  0.2  Iris-setosa


print("Indeksowanie kolumn")
print(df_4.head())
# bierzemy kolumnę 5.1 jako lista stringów to ocpja a
print(df_4['5.1'])
# 0      4.9
# 1      4.7
# 2      4.6
# 3      5.0
# 4      5.4
#       ...
# 144    6.7
# 145    6.3
# 146    6.5
# 147    6.2
# 148    5.9
# Name: 5.1, Length: 149, dtype: float64


#opcja nr 2 do dane.kolumna ale ak sa kropki to nie działa i pewnie w PyCharm też będzie problem w JD dziła

print("Indeksowanie kolumn df_4[['nazwa1','nazwa2']]")
print(df_4[['5.1', '3.5', '1.4', '0.2', 'Iris-setosa']])

#Name: 5.1, Length: 149, dtype: float64
#     5.1  3.5  1.4  0.2     Iris-setosa
#0    4.9  3.0  1.4  0.2     Iris-setosa
#1    4.7  3.2  1.3  0.2     Iris-setosa
#2    4.6  3.1  1.5  0.2     Iris-setosa
#3    5.0  3.6  1.4  0.2     Iris-setosa
#4    5.4  3.9  1.7  0.4     Iris-setosa
#..   ...  ...  ...  ...             ...
#144  6.7  3.0  5.2  2.3  Iris-virginica
#145  6.3  2.5  5.0  1.9  Iris-virginica
#46  6.5  3.0  5.2  2.0  Iris-virginica
#147  6.2  3.4  5.4  2.3  Iris-virginica
#148  5.9  3.0  5.1  1.8  Iris-virginica



print("Indeksowanie kolumn df_4i wierszy[1:4][['nazwa1','nazwa2']] ")
print(df_4[1:3][['5.1', '3.5', '1.4', '0.2', 'Iris-setosa']])

#Indeksowanie kolumn df_4i wierszy[1:4][['nazwa1','nazwa2']]
#   5.1  3.5  1.4  0.2  Iris-setosa
#1  4.7  3.2  1.3  0.2  Iris-setosa
#2  4.6  3.1  1.5  0.2  Iris-setosa