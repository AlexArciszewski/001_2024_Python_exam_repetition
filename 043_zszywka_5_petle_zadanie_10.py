# Zad. 10*
# Sprawdzanie, czy liczba jest doskonała.
# Napisz program, który sprawdzi, czy podana przez usera liczba jest doskonała.
# Liczba doskonała, to taka liczba, która jest sumą wszystkich swoich dzielników właściwych (czyli mniejszych od niej samej).
# Przykłady liczb doskonałych: 6 (6 = 1 + 2 + 3), 28, 496, 8128.
#
# Podpowiedź:
# Wykorzystaj instrukcje warunkowe i modulo (%)

k_box = []
master_number = int(input("?"))
for k in range(1, master_number + 1):
    if master_number % k == 0:
        k_box.append(k)
print(k_box)
k_box.pop(-1)
print(k_box)
sum = sum(k_box)
print(sum)

if sum == master_number:
    print(f"The {master_number} is that number")
else:
     print("U missed")