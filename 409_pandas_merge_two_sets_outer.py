#Zadanie 5. Połącz zbior_scalony razem ze zbiorem 3 na podstawie imion, tak aby zostały użyte wszystkie obserwacje.



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

#Aby połączyć zbiory biorąc pod uwagę wszystkie możliwe wartości występujące w obu zbiorach należy wykorzystać how = ‘outer’:

print(pd.merge(zbior_scalony, zbior3, on='Imię', how='outer'))


#      Imię   Waga  Wzrost    Miasto
#0     Adam  104.0     NaN       NaN
#1   Albert  105.0   185.0       NaN
#2  Andrzej   92.0   192.0  Warszawa
#3      Jan   77.0   180.0       NaN
#4   Janusz    NaN     NaN    Kraków
#5   Monika    NaN     NaN      Łódź
#6   Patryk   83.0     NaN       NaN
#7  Paulina    NaN     NaN    Kraków
#8    Paweł  115.0     NaN   Olsztyn
#9   Szymon   88.0   175.0  Warszawa