#Zadanie Wyświetl osoby, które są z Krakowa oraz mają czas biegu krótszy niż 2,2 lub mężczyzn, którzy mają ponad 190 cm wzrostu.



import pandas as pd
#Otwieram plik zawody

df = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\370_zawody.xlsx")



print('\n')

print(df)

#        Imię  Rzut  Skok  Czas biegu       Płeć Zawody    Miasto  Wzrost
#0   Karolina  8.03  3.13        2.11    Kobieta    Tak  Warszawa     188
#1    Mateusz  8.11  3.22        2.07  Mężczyzna    Tak    Kraków     178
#2    Paulina  7.44  2.98        2.08    Kobieta    Nie    Kraków     182
#3   Zdzisław  7.38  3.14        2.32  Mężczyzna    Nie  Warszawa     188
#4     Janusz  7.98  3.55        2.22  Mężczyzna    Tak    Gdańsk     192
#5       Ania  7.44  3.68        2.42    Kobieta    Nie  Warszawa     190
#6  Agnieszka  7.33  3.04        2.52    Kobieta    Nie    Kraków     191
#7    Natalia  7.23  2.74        2.11    Kobieta    Tak  Warszawa     179
#8      Kamil  6.59  2.94        2.98  Mężczyzna    Nie    Gdańsk     178
#9        Ewa  8.88  3.00        2.04    Kobieta    Tak  Warszawa     182


print('\n')

print(df[(df['Miasto'] == 'Warszawa') & (df['Płeć'] == 'Kobieta')])


#       Imię  Rzut  Skok  Czas biegu     Płeć Zawody    Miasto  Wzrost
#0  Karolina  8.03  3.13        2.11  Kobieta    Tak  Warszawa     188
#5      Ania  7.44  3.68        2.42  Kobieta    Nie  Warszawa     190
#7   Natalia  7.23  2.74        2.11  Kobieta    Tak  Warszawa     179
#9       Ewa  8.88  3.00        2.04  Kobieta    Tak  Warszawa     182

print('\n')

print(df[(df['Skok'] <= 3.1) & (df['Miasto'] == 'Warszawa')])

#      Imię  Rzut  Skok  Czas biegu     Płeć Zawody    Miasto  Wzrost
#7  Natalia  7.23  2.74        2.11  Kobieta    Tak  Warszawa     179
#9      Ewa  8.88  3.00        2.04  Kobieta    Tak  Warszawa     182


print(df[((df['Miasto'] == 'Kraków') & (df['Czas biegu'] < 2.2)) | ((df['Płeć'] == 'Mężczyzna') & (df['Wzrost'] > 188))])
#df[((df['Miasto'] == 'Kraków') & (df['Czas biegu'] < 2.2)) | ((df['Płeć'] == 'Mężczyzna') & (df['Wzrost']>190))]