#Za pomocą maski sprawdź, które osoby są z Warszawy.


import pandas as pd
#Otwieram plik zawody

df = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\370_zawody.xlsx")



print('\n')

print(df)

print('\n')

print(df[df['Miasto']=='Warszawa'])

#       Imię  Rzut  Skok  Czas biegu       Płeć Zawody    Miasto  Wzrost
#0  Karolina  8.03  3.13        2.11    Kobieta    Tak  Warszawa     188
#3  Zdzisław  7.38  3.14        2.32  Mężczyzna    Nie  Warszawa     188
#5      Ania  7.44  3.68        2.42    Kobieta    Nie  Warszawa     190
#7   Natalia  7.23  2.74        2.11    Kobieta    Tak  Warszawa     179
#9       Ewa  8.88  3.00        2.04    Kobieta    Tak  Warszawa     182