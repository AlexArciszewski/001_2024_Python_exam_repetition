# Zadanie 1. Stwórz tabelę danych o nazwie x , która wygląda następująco:

#                    Imie    Wiek
#Pierwsza osoba      Ania     18
#Druga osoba         Szymon   22
#Trzecia osoba       Paulina  33

import pandas as pd
#kolumny  index dla wierszy

x = {'Imie': pd.Series(['Ania', 'Szymon', 'Paulina'], index=['Pierwsza osoba', 'Druga osoba', 'Trzecia osoba']),
     'Wiek': pd.Series([18, 22, 33],  index=['Pierwsza osoba', 'Druga osoba', 'Trzecia osoba'])}

df = pd.DataFrame(x)
print(df)

#                   Imie  Wiek
# Pierwsza osoba     Ania    18
# Druga osoba      Szymon    22
# Trzecia osoba   Paulina    33