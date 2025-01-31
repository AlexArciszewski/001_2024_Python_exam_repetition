#Zadanie
#Oblicz minimalny i maksymalny czas biegu dla osób z różnych miast, które miały maksymalny skok na poziomie 3,1.


import pandas as pd


df = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\370_zawody.xlsx")


print(df[df["Skok"] <= 3.1].groupby('Miasto').agg({"Czas biegu":['min', 'max']}))

#                min   max
#Miasto
#Gdańsk         2.98  2.98
#Kraków         2.08  2.52
#Warszawa       2.04  2.11

