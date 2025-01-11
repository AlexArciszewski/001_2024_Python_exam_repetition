#Zadanie
#Zaimportuj dane będące w pliku *homework.csv*. Po zaimportowaniu danych zmień nazwy kolumn na:
# Imię, Nazwisko, Wzrost oraz Kolor oczu.



import pandas as pd



df = pd.read_csv(r"C:\Users\arcis\PycharmProjects\pythonProject25\364_homework.csv")
#print(df.head())

df.columns=['Imię', 'Nazwisko', 'Wzrost', 'Kolor oczu']

print(df.head())



#        Imię Nazwisko  Wzrost  Kolor oczu
# 0      Lucja      Lis     180  Niebieskie
# 1       Adam     Ziab     177       Szare
# 2  Agnieszka     Klos     156       Szare
# 3    Paulina    Zgryz     199     Zielone

#Zmiana indeksowania od pozycji 0 na od pozycji 1 używamy index

print('\n')

df = pd.read_csv(r"C:\Users\arcis\PycharmProjects\pythonProject25\364_homework.csv")
#print(df.head())

df.columns=['Imię', 'Nazwisko', 'Wzrost', 'Kolor oczu']
df.index = range(1, len(df) + 1)
print(df.head())


#         Imię Nazwisko  Wzrost  Kolor oczu
# 1      Lucja      Lis     180  Niebieskie
# 2       Adam     Ziab     177       Szare
# 3  Agnieszka     Klos     156       Szare
# 4    Paulina    Zgryz     199     Zielone