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

