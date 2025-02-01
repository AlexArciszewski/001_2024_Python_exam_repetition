#Zadanie 6. Zresetuj indeks w zbiorze_scalonym za pomocą odpowiedniej metody (użyj argumentu drop=True aby nie
# dodawać nowych kolumn powstałych z indeksu). Następnie stwórz podzbiór zbioru_scalonego wybierając jedynie
# rekordy, gdzie Waga > 90. Zapisz zbiór do zmiennej podzbior. Na powstałym podzbiorze wylicz bmi osób za pomocą
# wzoru: <code>Waga/(Wzrost w m)^2</code> i zapisz do zmiennej bmi.



import pandas as pd

zbior1 = pd.DataFrame({'Imię':['Szymon', 'Andrzej', 'Jan', 'Albert'],
                      'Waga':[88, 92, 77, 105],
                       'Wzrost': [175, 192, 180, 185]})

zbior2 = pd.DataFrame({'Imię':['Patryk','Paweł', 'Adam'],
                      'Waga':[83,115,104]})

zbior3 = pd.DataFrame({'Imię':['Andrzej','Janusz','Paweł','Szymon','Paulina','Monika'],
                            'Miasto':['Warszawa','Kraków','Olsztyn','Warszawa','Kraków','Łódź']})


zbior_scalony = pd.concat([zbior1, zbior2], keys=['Zbior 1', 'Zbior2'])
print(zbior_scalony)
#              Imię  Waga  Wzrost
#Zbior 1 0   Szymon    88   175.0
#        1  Andrzej    92   192.0
#        2      Jan    77   180.0
#        3   Albert   105   185.0
#Zbior2  0   Patryk    83     NaN
#        1    Paweł   115     NaN
#       2     Adam   104     NaN

#resetowanei indexu drop()

zbior_scalony =zbior_scalony.reset_index(drop=True)

print(zbior_scalony)

#      Imię  Waga  Wzrost
#0   Szymon    88   175.0
#1  Andrzej    92   192.0
#2      Jan    77   180.0
#3   Albert   105   185.0
#4   Patryk    83     NaN
#5    Paweł   115     NaN
#6     Adam   104     NaN

#Stwórz podzbiór zbioru_scalonego wybierając jedynie rekordy, gdzie Waga > 90.

podzbior = zbior_scalony[zbior_scalony['Waga']>90].copy()
print(podzbior)

#1  Andrzej    92   192.0
#3   Albert   105   185.0
#5    Paweł   115     NaN
#6     Adam   104     NaN

#Na powstałym podzbiorze wylicz bmi osób za pomocą wzoru: <code>Waga/(Wzrost w m)^2</code> i zapisz do zmiennej bmi.

podzbior['bmi'] = podzbior['Waga']/((podzbior['Wzrost']/100)*2)
print(podzbior)


#      Imię  Waga  Wzrost        bmi
#1  Andrzej    92   192.0  23.958333
#3   Albert   105   185.0  28.378378
#5    Paweł   115     NaN        NaN
#6     Adam   104     NaN        NaN


zbior_scalony  = zbior_scalony.join(podzbior['bmi'])

print(zbior_scalony)

#      Imię  Waga  Wzrost        bmi
#0   Szymon    88   175.0        NaN
#1  Andrzej    92   192.0  23.958333
#2      Jan    77   180.0        NaN
#3   Albert   105   185.0  28.378378
#4   Patryk    83     NaN        NaN
#5    Paweł   115     NaN        NaN
#6     Adam   104     NaN        NaN