# Zadanie Odpakuj powyższy obiekt za pomocą metody *.unstack*

import pandas as pd


df = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\370_zawody.xlsx")

print(df)
print(df.groupby(['Płeć', 'Miasto']).agg({'Wzrost': 'mean'}))

#                    Wzrost
#Płeć      Miasto
#Kobieta   Kraków    186.50
#          Warszawa  184.75
#Mężczyzna Gdańsk    185.00
#          Kraków    178.00
#          Warszawa  188.00

print('\n')

z = df.groupby(['Płeć', 'Miasto']).agg({'Wzrost': 'mean'})

print(z.unstack())


#         Wzrost
#Miasto    Gdańsk Kraków Warszawa
#Płeć
#Kobieta      NaN  186.5   184.75
#Mężczyzna  185.0  178.0   188.00