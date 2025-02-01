#Zadanie
#Dokonaj wczytania danych po raz kolejny, wykonując wszystkie operację z zadań 1-6 na etapie importowania.
import pandas as pd
def func(arg):
    if arg == 'Tak':
        return True
    else:
        return False


df = pd.read_excel(r"C:\Dane\2_ML_Projekty\003_programowanie_ML_zadanka_kurs_wprowadzenie\Moduł 2\Zbiory danych\zledane.xlsx",
                  skiprows=[1],
                  dtype={'Rzut':'float64',
                        'Skok':'float64',
                        'Czas biegu':'float64',
                        'Wzrost':'int64'},
                  converters={'Zawody':func})
df.info()

#Data columns (total 8 columns):
 #   Column      Non-Null Count  Dtype
#---  ------      --------------  -----
# 0   Imię        10 non-null     object
# 1   Rzut        10 non-null     float64
# 2   Skok        10 non-null     float64
# 3   Czas biegu  10 non-null     float64
# 4   Płeć        10 non-null     object
# 5   Zawody      10 non-null     bool
# 6   Miasto      10 non-null     object
# 7   Wzrost      10 non-null     int64
#dtypes: bool(1), float64(3), int64(1), object(3)
#memory usage: 702.0+ bytes