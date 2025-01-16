# Data frames dane wielowymairowe macierze danych z nazwami kolumn oraz etykiet wierszyjak w excel
#Tworzenie
#1.Ze słownika list klucz nazwa kolumn wartoscia sa listy wartosci,listy musza byc tejs amej dulogsci
#2.lista slowników klucz wartosci za kazdym razem trzeba powtórzyć
#3. z dwuwymairowych np.array([['wartosc','wartosc']])


import pandas as pd

print("\n sposob nr1.\n")
#1 ze slownika list...

slownik = {
    'wojewodztwo': ['Mazowieckie','Warminsko-Mazurskie', 'Podlaskie','Pomorskie', 'małopolskie'],
    'stolica': ['Warszawa', 'Olsztyn', 'Białystok', 'Gdańsk', 'Kraków'],
    'l_ludnosci': [5.42, 1.42, 1.18, 2.35, 3.41]
}

print(slownik)

#przekształcamy dane

df = pd.DataFrame(slownik)
print(df)

#           wojewodztwo    stolica  l_ludnosci
#0          Mazowieckie   Warszawa        5.42
#1  Warminsko-Mazurskie    Olsztyn        1.42
#2            Podlaskie  Białystok        1.18
#3            Pomorskie     Gdańsk        2.35
#4          małopolskie     Kraków        3.41


#zmieniamy nazwy indeksów zautomatu są liczbowe 0,1,2,3,4
#używamy metody index

print(df.index)
#RangeIndex(start=0, stop=5, step=1)


#zmiana:
df.index = [1, 2, 3, 4, 5]
print(df.index)

print(df)
#zmiana się zapisała

#           wojewodztwo    stolica  l_ludnosci
#1          Mazowieckie   Warszawa        5.42
#2  Warminsko-Mazurskie    Olsztyn        1.42
#3            Podlaskie  Białystok        1.18
#4            Pomorskie     Gdańsk        2.35
#5          małopolskie     Kraków        3.4

df.index = ['MAZ', 'WM', 'POD', 'POM', 'MAL']

print(df)



#             wojewodztwo    stolica  l_ludnosci
#MAZ          Mazowieckie   Warszawa        5.42
#WM   Warminsko-Mazurskie    Olsztyn        1.42
#POD            Podlaskie  Białystok        1.18
#POM            Pomorskie     Gdańsk        2.35
#MAL          małopolskie     Kraków        3.41
print("\n sposob nr1.2 \n")
# sposób nr 1.2 Słownik dajemy do df ale równiez indeksy,które chcemy zrobić wpisujac jek
slownik2 = {
    'wojewodztwo': pd.Series(['Mazowieckie','Warminsko-Mazurskie', 'Podlaskie','Pomorskie', 'małopolskie'],
                             index = ['MAZ', 'WM', 'POD', 'POM', 'MAL']),
    'stolica': ['Warszawa', 'Olsztyn', 'Białystok', 'Gdańsk', 'Kraków'],
    'l_ludnosci': [5.42, 1.42, 1.18, 2.35, 3.41]
}
df = pd.DataFrame(slownik2)
print(df)


#             wojewodztwo    stolica  l_ludnosci
#MAZ          Mazowieckie   Warszawa        5.42
#WM   Warminsko-Mazurskie    Olsztyn        1.42
#POD            Podlaskie  Białystok        1.18
#POM            Pomorskie     Gdańsk        2.35
#MAL          małopolskie     Kraków        3.41


print("\n przestawianie kolumn \n")


slownik2 = {
    'wojewodztwo': pd.Series(['Mazowieckie','Warminsko-Mazurskie', 'Podlaskie','Pomorskie', 'małopolskie'],
                             index = ['MAZ', 'WM', 'POD', 'POM', 'MAL']),
    'stolica': ['Warszawa', 'Olsztyn', 'Białystok', 'Gdańsk', 'Kraków'],
    'l_ludnosci': [5.42, 1.42, 1.18, 2.35, 3.41]
}
df = pd.DataFrame(slownik2,columns = ['stolica','l_ludnosci','wojewodztwo'])
print(df)

#       stolica  l_ludnosci          wojewodztwo
#MAZ   Warszawa        5.42          Mazowieckie
#WM     Olsztyn        1.42  Warminsko-Mazurskie
#POD  Białystok        1.18            Podlaskie
#POM     Gdańsk        2.35            Pomorskie
#MAL     Kraków        3.41          małopolskie
