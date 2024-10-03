# Działa podobnie jak list comprehension, ale zwraca zbiór (unikalne wartości).
# Stworzenie zbioru liczb parzystych:


even_numbers_set = {x for x in range(10) if x % 2 == 0}
print(even_numbers_set)
# {0, 2, 4, 6, 8}