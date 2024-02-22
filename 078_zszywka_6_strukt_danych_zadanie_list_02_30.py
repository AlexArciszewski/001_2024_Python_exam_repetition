# Zad 3.
# Napisz program, który będzie pracował z trzema listami:
# lista1 = ["abc", "def", "ghi", "jkl"]
# lista2 = [1, 2, 3, 4, 5]
# lista3 = ["xyz", 1, '2']
#
# Niech program:
# • wydrukuje te listy
# • wydrukuje pierwszy oraz czwarty element z lista1
# • przypisze drugiemu elementowi lista2 wartości drugiego elementu z lista3
# • przypisze trzeciemu elementowi lista3 wartość tekstową wpisaną z klawiatury
# • doda nowy element ‘słowo’ do lista1 za pomocą metody .append()
# • skasuje element o indeksie 2 z lista1
# • wyznaczy liczbę elementów lista3
# • powiększy lista1 o elementy lista3
# Po każdej przeprowadzonej zmianie wydrukuje zmienioną listę.


lista1 = ["abc", "def", "ghi", "jkl"]
lista2 = [1, 2, 3, 4, 5]
lista3 = ["xyz", 1, '2']

# • wydrukuje te listy
print(lista1, lista2, lista3)
# ['abc', 'def', 'ghi', 'jkl'] [1, 2, 3, 4, 5] ['xyz', 1, '2']

# • wydrukuje pierwszy oraz czwarty element z lista1
print(lista1[0], lista1[3])
# abc jkl

# • przypisze drugiemu elementowi lista2 wartości drugiego elementu z lista3
lista2[1] = lista3[1]
print(lista2)
# [1, 1, 3, 4, 5]

# • przypisze trzeciemu elementowi lista3 wartość tekstową wpisaną z klawiatury
x = input("pls write sth: ")
lista3[2] = x
print(lista3)
#a as input ['xyz', 1, 'a']

# doda nowy element ‘słowo’ do lista1 za pomocą metody .append()
lista1.append('slowo')
print(lista1)
# ['abc', 'def', 'ghi', 'jkl', 'slowo']

# • skasuje element o indeksie 2 z lista1
lista1.remove(lista1[2])
print(lista1)
# ['abc', 'def', 'jkl', 'slowo']

# • wyznaczy liczbę elementów lista3
print(len(lista3))
# 3

# • powiększy lista1 o elementy lista3
lista1.extend(lista3)
print(lista1)
# ['abc', 'def', 'jkl', 'slowo', 'xyz', 1, 'a']


# Po każdej przeprowadzonej zmianie wydrukuje zmienioną listę.
# ???????zmianie czego i gdzie?
