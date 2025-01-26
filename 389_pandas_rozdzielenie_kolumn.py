#Z powrotem rozdziel kolumnę "Imię + Płeć" na dwie oddzielne kolumny. Nazwij pierwszą kolumnę "Rozdzielone Imię" a drugą "Rozdzielona Płeć".

import pandas as pd
import numpy as np

df = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\370_zawody.xlsx")

df['Dobry czas'] = 0

df['Dobry czas'] = np.where(df['Czas biegu'] < 2.2, 'TAK', 'NIE')


df = df.rename(columns={'Miasto':'Miejscowość', 'Czas biegu':'Bieg'})


print(df)
print('\n')

df.drop('Dobry czas', axis=1, inplace=True)

print(df)


#        Imię  Rzut  Skok  Bieg       Płeć Zawody Miejscowość  Wzrost
#0   Karolina  8.03  3.13  2.11    Kobieta    Tak    Warszawa     188
#1    Mateusz  8.11  3.22  2.07  Mężczyzna    Tak      Kraków     178
#2    Paulina  7.44  2.98  2.08    Kobieta    Nie      Kraków     182
#3   Zdzisław  7.38  3.14  2.32  Mężczyzna    Nie    Warszawa     188
#4     Janusz  7.98  3.55  2.22  Mężczyzna    Tak      Gdańsk     192
#5       Ania  7.44  3.68  2.42    Kobieta    Nie    Warszawa     190
#6  Agnieszka  7.33  3.04  2.52    Kobieta    Nie      Kraków     191
#7    Natalia  7.23  2.74  2.11    Kobieta    Tak    Warszawa     179
#8      Kamil  6.59  2.94  2.98  Mężczyzna    Nie      Gdańsk     178
#9        Ewa  8.88  3.00  2.04    Kobieta    Tak    Warszawa     182


df['Imię + Płeć'] = df['Imię'] + ' ' +df['Płeć']

print("\n")

print(df)

#        Imię  Rzut  Skok  Bieg  ... Zawody Miejscowość Wzrost         Imię + Płeć
#0   Karolina  8.03  3.13  2.11  ...    Tak    Warszawa    188    Karolina Kobieta
#1    Mateusz  8.11  3.22  2.07  ...    Tak      Kraków    178   Mateusz Mężczyzna
#2    Paulina  7.44  2.98  2.08  ...    Nie      Kraków    182     Paulina Kobieta
#3   Zdzisław  7.38  3.14  2.32  ...    Nie    Warszawa    188  Zdzisław Mężczyzna
#4     Janusz  7.98  3.55  2.22  ...    Tak      Gdańsk    192    Janusz Mężczyzna
#5       Ania  7.44  3.68  2.42  ...    Nie    Warszawa    190        Ania Kobieta
#6  Agnieszka  7.33  3.04  2.52  ...    Nie      Kraków    191   Agnieszka Kobieta
#7    Natalia  7.23  2.74  2.11  ...    Tak    Warszawa    179     Natalia Kobieta
#8      Kamil  6.59  2.94  2.98  ...    Nie      Gdańsk    178     Kamil Mężczyzna
#9        Ewa  8.88  3.00  2.04  ...    Tak    Warszawa    182         Ewa Kobieta


print("\n")

df[['Rozdzielone Imię', 'Rozdzielona Płeć']] = df['Imię + Płeć'].str.split(' ', expand=True)
df.drop('Imię + Płeć', axis=1, inplace=True)
print(df)

#        Imię  Rzut  Skok  ...  Wzrost Rozdzielone Imię Rozdzielona Płeć
#0   Karolina  8.03  3.13  ...     188         Karolina          Kobieta
#1    Mateusz  8.11  3.22  ...     178          Mateusz        Mężczyzna
#2    Paulina  7.44  2.98  ...     182          Paulina          Kobieta
#3   Zdzisław  7.38  3.14  ...     188         Zdzisław        Mężczyzna
#4     Janusz  7.98  3.55  ...     192           Janusz        Mężczyzna
#5       Ania  7.44  3.68  ...     190             Ania          Kobieta
#6  Agnieszka  7.33  3.04  ...     191        Agnieszka          Kobieta
#7    Natalia  7.23  2.74  ...     179          Natalia          Kobieta
#8      Kamil  6.59  2.94  ...     178            Kamil        Mężczyzna
#9        Ewa  8.88  3.00  ...     182              Ewa          Kobieta