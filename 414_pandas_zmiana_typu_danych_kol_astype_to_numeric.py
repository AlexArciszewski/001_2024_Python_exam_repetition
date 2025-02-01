#Zadanie Zamień kolumny "Rzut", "Skok" oraz "Czas biegu" na float64 za pomocą *astype*.

import pandas as pd

df = pd.read_excel(r"C:\Dane\2_ML_Projekty\003_programowanie_ML_zadanka_kurs_wprowadzenie\Moduł 2\Zbiory danych\zledane.xlsx")

print(df.head())


#       Imię     Rzut     Skok Czas biegu       Płeć  Zawody    Miasto Wzrost
#0    String  Float64  Float64    Float64     String  String    String  Int64
#1  Karolina     8.03     3.13       2.11    Kobieta     Tak  Warszawa    188
#2   Mateusz     8.11     3.22       2.07  Mężczyzna     Tak    Kraków    178
#3   Paulina     7.44     2.98       2.08    Kobieta     Nie    Kraków    182
#4  Zdzisław     7.38     3.14       2.32  Mężczyzna     Nie  Warszawa    188

print('\n')
#print(df.info())

df.info()
#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 11 entries, 0 to 10
#Data columns (total 8 columns):
 #   Column      Non-Null Count  Dtype
#---  ------      --------------  -----
# 0   Imię        11 non-null     object
# 1   Rzut        11 non-null     object
# 2   Skok        11 non-null     object
# 3   Czas biegu  11 non-null     object
# 4   Płeć        11 non-null     object
# 5   Zawody      11 non-null     object
# 6   Miasto      11 non-null     object
# 7   Wzrost      11 non-null     object
#dtypes: object(8)
#memory usage: 836.0+ bytes

#df['Rzut'] = df['Rzut'].astype('float64')
#df['Skok'] = df['Skok'].astype('float64')
#df['Czas biegu'] = df['Czas biegu'].astype('float64')

#df.info()
#błąd


print(df['Rzut'].unique())

#coerce = Powoduje zamianę problematycznych wartości na NaN, zamiast zgłaszania błędu.
df['Skok'] = pd.to_numeric(df['Skok'], errors='coerce')
df['Rzut'] = pd.to_numeric(df['Rzut'], errors='coerce')
df['Czas biegu'] = pd.to_numeric(df['Czas biegu'], errors='coerce')

print('\n')

df.info()



#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 11 entries, 0 to 10
#Data columns (total 8 columns):
 #   Column      Non-Null Count  Dtype
#---  ------      --------------  -----
# 0   Imię        11 non-null     object
# 1   Rzut        10 non-null     float64
# 2   Skok        10 non-null     float64
# 3   Czas biegu  10 non-null     float64
# 4   Płeć        11 non-null     object
# 5   Zawody      11 non-null     object
# 6   Miasto      11 non-null     object
# 7   Wzrost      11 non-null     object
#dtypes: float64(3), object(5)
#memory usage: 836.0+ bytes