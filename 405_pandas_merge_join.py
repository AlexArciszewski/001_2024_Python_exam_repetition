#Zadanie
#Połącz zbior1 i zbior2 tak aby obserwacje jednego znajdowały się nad obserwacjami drugiego
# (uwzględnij wszystkie obserwacje). Nazwij to zbior_scalony.



import pandas as pd

zbior1 = pd.DataFrame({'Imię':['Szymon', 'Andrzej', 'Jan', 'Albert'],
                      'Waga':[88, 92, 77, 105],
                       'Wzrost': [175, 192, 180, 185]})

zbior2 = pd.DataFrame({'Imię':['Patryk','Paweł', 'Adam'],
                      'Waga':[83,115,104]})

zbior3 = pd.DataFrame({'Imię':['Andrzej','Janusz','Paweł','Szymon','Paulina','Monika'],
                            'Miasto':['Warszawa','Kraków','Olsztyn','Warszawa','Kraków','Łódź']})


print(zbior1)


zbior_scalony = pd.concat([zbior1, zbior2])
print(zbior_scalony)


#      Imię  Waga  Wzrost
#0   Szymon    88     175
#1  Andrzej    92     192
#2      Jan    77     180
#3   Albert   105     185
#      Imię  Waga  Wzrost
#0   Szymon    88   175.0
#1  Andrzej    92   192.0
#2      Jan    77   180.0
#3   Albert   105   185.0
#0   Patryk    83     NaN
#1    Paweł   115     NaN
#2     Adam   104     NaN






















