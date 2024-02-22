# Zad 2.
# Utwórz zbiór składający się z 15 losowo wygenerowanych wartości typu int z przedziału 5 - 120.
# Następnie usuń ze zbioru wszystkie liczby parzyste.

import random



random_numbers = []
chosen_number = []
for i in range(15):
    j = random.randint(5,121)
    random_numbers.append(j)
print(random_numbers)

for number in random_numbers:
    if number % 2 != 0:
        chosen_number.append(number)
print(chosen_number)
