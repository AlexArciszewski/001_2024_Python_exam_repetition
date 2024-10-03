numbers = []
for i in range(25):
    numbers.append(i)
print(numbers)


even_numbers1 = []
for n in numbers:
    if n % 2 == 0:
        even_numbers1.append(n)
print(even_numbers1)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]


numbers2 = []
for n in range(25):
    numbers2.append(n)
even_numbers_2 = [a for a in numbers2 if a % 2 == 0]
print(even_numbers_2)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]


squares = []

for number in range(10):
    squares.append(number ** 2)
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares2 = [b**2 for b in range(10)]
print(squares2)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Zadanie:
# Masz listę imion, a Twoim zadaniem jest stworzenie nowej listy,
# która zawiera tylko imiona zaczynające się na literę "A" i
# zapisane są wielkimi literami.

names = ["Anna", "Barbara", "Andrzej", "Zenon", "Alicja", "Jan"]


chosen_names = [ name.upper() for name in names if name[0] =="A"]
print(chosen_names)




