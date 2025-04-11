# 1. Dodawanie na końcu.

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
# [1, 2, 3, 4]


# 2. Wydłużanie na końcu.

my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)
# [1, 2, 3, 4, 5, 6]


# 3. insert umeiszczanie elementu w konkretnym miejscu.

my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)
# [1, 4, 2, 3]


# 4.remove usuniecie pierwszego wskazanego elementu.

my_list = [1, 2, 3, 2]
my_list.remove(2)

print(my_list)
# [1, 3, 2]


# 5.pop() usunięcie i zwórcenie konkretnego elementu z lsity

my_list = [1, 2, 3, 4]
popped_element = my_list.pop(1)

print(my_list)
# .[1, 3, 4] usunięcie elementu z pozycji nr 1 czyli drugiego od lewej jest nim (2)
print(popped_element)
# 2


# 6 index() zwrocenie indexu danego elementu pierwszego od lewej
my_list = [1, 2, 3, 4]
index_of_two = my_list.index(2)
print(index_of_two)
# 1


# 7 count() metoda zwraca numer ile razy dany element był w danej liście.

my_list = [1, 2, 3, 2, 4, 2]
count_of_two = my_list.count(2)

print(count_of_two)
# 3


# 8 sort()metoda sortowanie rosnące.
my_list = [3, 1, 2, 5, 4]
my_list.sort()

print(my_list)
# [1, 2, 3, 4, 5]


# 9 reverse() sortowanie malejące

my_list = [1, 2, 3, "one", "two"]
my_list.reverse()

print(my_list)
# ['two', 'one', 3, 2, 1]


# 10 copy płytka kopia bez zmian w oryginale.

my_list = [1, 2, 3]
my_list_copy = my_list.copy()

print(my_list)
print(my_list_copy)

my_list_copy.append(4)

print(my_list)
print(my_list_copy)

# [1, 2, 3]
# [1, 2, 3, 4]


# 11 update aktualizacja elemnetu na danej pozycji w liscie

my_list = [1, 2, 3, 4, 5]
my_list[2] = 10

print(my_list)
# [1, 2, 10, 4, 5] na pozycji w nawiasie kwadratowym w lsite włacza sie element


# 12 sort(reverse =True/False)metoda sortowanie rosnące.

my_list = [3, 1, 2, 5, 4]
my_list.sort(reverse=True)

print(my_list)
# [5, 4, 3, 2, 1]

a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a, reverse=True)
print(x)
# ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']


# 13 print(len(list)) metoda sortowanie rosnące.

my_list = [3, 1, 2, 5, 2, 4]
print(len(my_list))

# 6 jest 6 elementów


# 14 lista.pop(len(lista) -1) usuniecie ostatniego elementu

my_list = [3, 1, 2, 5, 2, 4]
print(len(my_list))
# 6
my_list.pop(len(my_list) - 1)
print(my_list)

print(len(my_list))
# 5


# 15 max i min el.listy

my_list = [3, 1, 2, 5, 2, 4]

print(max(my_list))

# max wartośc 5
print(min(my_list))

# min wartośc 5


# 16 lista.insert(a,b) na pozycję a wstaw b

my_list = [3, 1, 2, 5, 2, 4]

my_list.insert(0, 100)
print(my_list)

# [100, 3, 1, 2, 5, 2, 4]


# BONUS! Python slicing for string!!!


print("word"[
      ::-1])  # pierwsze ":" nie ma pozycji startu lecimy od poczatku, drugie ":" nie ma endu czyli lecimy domyślnie od końca, -1 to step od końca po jednej literce.
# wynik to: drow


# 17: numer max index z listy
nums = [4, 6, 8, 24, 12, 2]


def max_element_pos(nums):
    max_index = nums.index(max(nums))
    return max_index


print(max_element_pos(nums))

# in not in
a = [3, 1, 5, 7, 9, 2, 6]

# j) 8 in a
print(8 in a)
# False

# k) 4 not in a
print(4 not in a)
# True

# #Dict z list
# dict_of_words = dict(zip(list_of_words, list_of_reps))
# print(dict_of_words)
#
#
# dict2_of_words = {}
#
# for i in range(len(list_of_words)):
#     dict2_of_words[list_of_words[i]] = list_of_reps[i]
# print(dict2_of_words)

# List comprehensions

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers1 = []
for n in numbers:
    if n %2 == 0:
        # print(n)
        even_numbers1.append(n)
even_numbers1


# Sumowanie sum()
pensje = {'ksiegowa': 5000, 'kierowca': 4500, 'recepcjonistka': 4000}

sum_salary = []
for values in pensje.values():
    sum_salary.append(values)

total = sum(sum_salary)
print(total)

# Odwracanie list
odwroc_mnie = ['trudne', 'takie', 'bylo', 'nie', 'To']
odwrocona = odwroc_mnie
odwroc_mnie.reverse()

print(odwrocona)

odwroc_mnie = ['trudne', 'takie', 'bylo', 'nie', 'To']
print(odwroc_mnie[::-1])


odwroc_mnie = ['trudne', 'takie', 'bylo', 'nie', 'To']
odwrocona = []
for string in odwroc_mnie:
    odwrocona.insert(0, string)
print(odwrocona)

odwroc_mnie = ['trudne', 'takie', 'bylo', 'nie', 'To']
odwrocona = list(reversed(odwroc_mnie))
print(odwrocona)
print(" ".join(odwrocona))


# Zad 2.
# Utwórz zbiór składający się z 15 losowo wygenerowanych wartości typu int z przedziału
# 5 - 120. Następnie usuń ze zbioru wszystkie liczby parzyste.



import random


some_list = []
for num in range(5, 200):
    some_list.append(num)

chosen_list = []
for _ in range(15):
    chosen_num = random.choice(some_list)
    chosen_list.append(chosen_num)
print(chosen_list)
for number in chosen_list[:]: #kopia listy [:]
    if number % 2 == 0:
        chosen_list.remove(number)
print(f"{chosen_list} lista")
chosen_set = set(chosen_list)
print(chosen_set)




#Opcja B:


# # Iteracja po liście w odwrotnej kolejności
# for i in range(len(some_list) - 1, -1, -1):
#     if some_list[i] % 2 == 0:  # Sprawdzamy, czy liczba jest parzysta
#         del some_list[i]  # Usuwamy parzysty element
#
# print(some_list)
#
# #Opcja C:
# lista = [78, 115, 126, 172, 12, 198, 109, 183, 139, 126, 161, 55, 33, 130, 90]
#
# # Używamy list comprehension do utworzenia nowej listy bez parzystych liczb
# lista = [element for element in lista if element % 2 != 0]
#
# print(lista)




