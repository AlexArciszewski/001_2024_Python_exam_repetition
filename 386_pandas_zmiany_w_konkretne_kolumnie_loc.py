#Zadanie 1.  Przypisz osobom, które mają czas biegu krótszy niż 2.2 wartość "TAK" w kolumnie "Dobry czas". Pozostałym osobom wpisz wartość "NIE".
import pandas as pd



#Otwieram plik zawody

df = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\370_zawody.xlsx")


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


df['Dobry czas'] = 0


print('\n')

print(df)


df.loc[df['Czas biegu'] < 2.2, 'Dobry czas'] = 'TAK'
df.loc[df['Czas biegu'] >= 2.2,'Dobry czas'] = 'NIE'
df
print(df)

print('\n')

print('Opcja nr 2 numpy where')

print('\n')

import numpy as np


df2 = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\370_zawody.xlsx")

df2['Dobry czas'] = 0
print(df2)

print('\n')

df2['Dobry czas'] = np.where(df2['Czas biegu'] < 2.2, 'TAK', 'NIE')

print(df2)


#        Imię  Rzut  Skok  Czas biegu  ... Zawody    Miasto Wzrost  Dobry czas
#0   Karolina  8.03  3.13        2.11  ...    Tak  Warszawa    188         TAK
#1    Mateusz  8.11  3.22        2.07  ...    Tak    Kraków    178         TAK
#2    Paulina  7.44  2.98        2.08  ...    Nie    Kraków    182         TAK
#3   Zdzisław  7.38  3.14        2.32  ...    Nie  Warszawa    188         NIE
#4     Janusz  7.98  3.55        2.22  ...    Tak    Gdańsk    192         NIE
#5       Ania  7.44  3.68        2.42  ...    Nie  Warszawa    190         NIE
#6  Agnieszka  7.33  3.04        2.52  ...    Nie    Kraków    191         NIE
#7    Natalia  7.23  2.74        2.11  ...    Tak  Warszawa    179         TAK
#8      Kamil  6.59  2.94        2.98  ...    Nie    Gdańsk    178         NIE
#9        Ewa  8.88  3.00        2.04  ...    Tak  Warszawa    182         TAK