# Zadanie 2. Stwórz drugą tabelę, która będzie wyglądała w następujący sposób:
import numpy as np
#                     Imie    Wiek
# Czwarta osoba       Paulina  NaN
# Druga osoba         Szymon   22.0
# Pierwsza osoba      Ania     18.0
# Trzecia osoba       Nan      33


import pandas as pd
#     nazwy kolumny                   zawartosc kolumn                            nazwy wierwszy
y = {'Imie': pd.Series(['Paulina', 'Szymon', 'Ania', 'NaN'], index=['Czwarta osoba', 'Druga osoba', 'Pierwsza osoba', 'Trzecia osoba']),
     'Wiek': pd.Series(['Nan', 22.0, 18.0, 33], index=['Czwarta osoba', 'Druga osoba', 'Pierwsza osoba', 'Trzecia osoba'])}

df2 = pd.DataFrame(y)
print(df2)

#                    Imie  Wiek
# Czwarta osoba   Paulina   Nan
# Druga osoba      Szymon  22.0
# Pierwsza osoba     Ania  18.0
# Trzecia osoba       NaN    33
