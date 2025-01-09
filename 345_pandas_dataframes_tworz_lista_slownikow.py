#2.lista slowników klucz wartosci za kazdym razem trzeba powtórzyć

import pandas as pd

slownik = {
    'wojewodztwo': ['Mazowieckie','Warminsko-Mazurskie', 'Podlaskie','Pomorskie', 'Małopolskie'],
    'stolica': ['Warszawa', 'Olsztyn', 'Białystok', 'Gdańsk', 'Kraków'],
    'l_ludnosci': [5.42, 1.42, 1.18, 2.35, 3.41]
}
print(slownik)


lista_slownikow = [
    {'wojewodztwo': 'Mazowieckie', 'stolica': 'Warszawa','l_ludnosci': 5.42 },
    {'wojewodztwo': 'Warminsko-Mazurskie', 'stolica': 'Olsztyn','l_ludnosci': 1.42 },
    {'wojewodztwo': 'Podlaskie', 'stolica': 'Białystok','l_ludnosci': 1.18 },
    {'wojewodztwo': 'Pomorskie', 'stolica': 'Gdańsk','l_ludnosci': 2.35 },
    {'wojewodztwo': 'Małopolskie', 'stolica': 'Kraków','l_ludnosci': 3.41 },
]
#kazdy slownik odnosi sie do oddzielnego wiersza

print(lista_slownikow)
df=pd.DataFrame(lista_slownikow)
print(df)