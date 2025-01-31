#Zadanie
# Policz średni rzut, maksymalny rzut, średni czas biegu oraz minimalny czas biegu dla kobiet i mężczyzn.


import pandas as pd


df = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\370_zawody.xlsx")


print(df.groupby('Płeć').agg({
    "Rzut": ['mean', 'max'],
    "Czas biegu": ['mean', 'min'],
    }))

#            Rzut       Czas biegu
#            mean   max       mean   min
#Płeć
#Kobieta    7.725  8.88   2.213333  2.04
#Mężczyzna  7.515  8.11   2.397500  2.07