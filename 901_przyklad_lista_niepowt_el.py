# Pytanie 1 - lista niepowtarzalnych elementów
# Korzystając z podanej listy A
# stwórz listę B zawierającą tylko unikalne elementy z listy A

# A = [1,2,3,3,2,1,2,3] # -> B = [1,2,3]

# Opcja ciekawsza

list_a = [1, 2, 3, 3, 2, 1, 2, 3]
list_b = []
for number in list_a:
    if number not in list_b:
        list_b.append(number)
print(list_b)

# Wynik to [1, 2, 3]


# Opcja szybsza ale bez pętli...

set_a = set(list_a)
print(set_a)
list_c = list(set_a)
print(list_c)

# Wynik to [1, 2, 3]


# Opcja inna

list_a = [1, 2, 3, 3, 2, 1, 2, 3]
list_b = []

i = 0
k = len(list_a)

while i < k:
    if list_a[i] not in list_b:
        list_b.append(list_a[i])
    i += 1  # następny el.

print(list_b)

# Wynik to [1, 2, 3]
