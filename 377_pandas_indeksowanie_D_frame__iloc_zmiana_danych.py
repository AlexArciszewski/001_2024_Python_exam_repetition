#Za pomocą *iloc* zmień wzrost ostatnich trzech osób na 180 cm, 170 cm oraz 190 cm.
import pandas as pd
#Otwieram plik zawody

df = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\370_zawody.xlsx")



print('\n')

print(df)


#   Imię  Rzut  Skok  Czas biegu       Płeć Zawody    Miasto  Wzrost
#0   Karolina  8.03  3.13        2.11    Kobieta    Tak  Warszawa     188
#1    Mateusz  8.11  3.22        2.07  Mężczyzna    Tak    Kraków     178
#2    Paulina  7.44  2.98        2.08    Kobieta    Nie    Kraków     182
#3   Zdzisław  7.38  3.14        2.32  Mężczyzna    Nie  Warszawa     188
#4     Janusz  7.98  3.55        2.22  Mężczyzna    Tak    Gdańsk     170
#5       Ania  7.44  3.68        2.42    Kobieta    Nie  Warszawa     190
#6  Agnieszka  7.33  3.04        2.52    Kobieta    Nie    Kraków     191
#7    Natalia  7.23  2.74        2.11    Kobieta    Tak  Warszawa     179
#8      Kamil  6.59  2.94        2.98  Mężczyzna    Nie    Gdańsk     178
#9        Ewa  8.88  3.00        2.04    Kobieta    Tak  Warszawa     182

print('\n')

print(df.iloc[-3:])
#trzy ostatnie wiersze

#      Imię  Rzut  Skok  Czas biegu       Płeć Zawody    Miasto  Wzrost
#7  Natalia  7.23  2.74        2.11    Kobieta    Tak  Warszawa     179
#8    Kamil  6.59  2.94        2.98  Mężczyzna    Nie    Gdańsk     178
#9      Ewa  8.88  3.00        2.04    Kobieta    Tak  Warszawa     182


print('\n')

print(df.iloc[-3:]['Wzrost'])

#7    179
#8    178
#9    182
#Name: Wzrost, dtype: int64

#zmiana z użyciem get_loc
df.iloc[-3:, df.columns.get_loc('Wzrost')] = [180, 170, 190]

print(df.iloc[-3:]['Wzrost'])