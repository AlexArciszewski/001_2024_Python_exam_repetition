# Pytanie 3 - napisz kod, który zaprezentuje najważniejsze różnice między listą a tuplą


my_list = [1, 2, True, (1, 2)]

my_tuple = (1, 2, 3, 4, True, [1, 2])

# Lista zawierać może tuple słownik i inne struktury danych. Tupla też może zawierać inne struktury danych w tym listę


# lista jest mutowalna a tupla nie:


my_list = [1, 2, True, (1, 2)]
print(my_list)
print(f"Changing second element in{my_list}")
my_list[1] = 'kot'
print(my_list)

my_tuple = (1, 2, 3, 4, True, [1, 2])
print(my_tuple)
print(f"trying to change element in {my_tuple}")

try:
    my_tuple[1] = 'kot'
except TypeError as error:
    print(f"An error appeared {error} so the tuple is immutable")


print(my_tuple)