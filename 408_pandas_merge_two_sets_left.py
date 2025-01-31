#Zadanie 4. Połącz zbior_scalony razem ze zbiorem 3 na podstawie imion, tak aby zostały użyte jedynie obserwacje,
# które znajdują się w zbiorze scalonym.


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


#zbior scalony ze zbiorem 3 left czyli na podstawie wartosci w jednym zbiorze zbiorze_scalonym ktorymi sa imiona
pd.merge(zbior_scalony, zbior3, how='left', on='Imię')


#              Imię  Waga  Wzrost
#Zbior 1 0   Szymon    88   175.0
#        1  Andrzej    92   192.0
#        2      Jan    77   180.0
#        3   Albert   105   185.0
#Zbior2  0   Patryk    83     NaN
#        1    Paweł   115     NaN
#        2     Adam   104     NaN