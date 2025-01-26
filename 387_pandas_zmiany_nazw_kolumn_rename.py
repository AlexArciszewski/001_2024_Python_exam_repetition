#Zadanie Zmień nazwę kolumny "Miasto" na "Miejscowość" oraz "Czas biegu" na "Bieg".

import pandas as pd
import numpy as np

df = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\370_zawody.xlsx")

df['Dobry czas'] = 0

df['Dobry czas'] = np.where(df['Czas biegu'] < 2.2, 'TAK', 'NIE')


df = df.rename(columns={'Miasto':'Miejscowość', 'Czas biegu':'Bieg'})


print(df)


#        Imię  Rzut  Skok  Bieg       Płeć Zawody Miejscowość  Wzrost Dobry czas
#0   Karolina  8.03  3.13  2.11    Kobieta    Tak    Warszawa     188        TAK
#1    Mateusz  8.11  3.22  2.07  Mężczyzna    Tak      Kraków     178        TAK
#2    Paulina  7.44  2.98  2.08    Kobieta    Nie      Kraków     182        TAK
#3   Zdzisław  7.38  3.14  2.32  Mężczyzna    Nie    Warszawa     188        NIE
#4     Janusz  7.98  3.55  2.22  Mężczyzna    Tak      Gdańsk     192        NIE
#5       Ania  7.44  3.68  2.42    Kobieta    Nie    Warszawa     190        NIE
#6  Agnieszka  7.33  3.04  2.52    Kobieta    Nie      Kraków     191        NIE
#7    Natalia  7.23  2.74  2.11    Kobieta    Tak    Warszawa     179        TAK
#8      Kamil  6.59  2.94  2.98  Mężczyzna    Nie      Gdańsk     178        NIE
#9        Ewa  8.88  3.00  2.04    Kobieta    Tak    Warszawa     182        TAK