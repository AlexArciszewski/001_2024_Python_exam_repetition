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

numbers = [1,2,3,4]

new_list = []
print(new_list)
new_list = [x for x in numbers]
print(new_list)
another_new_list = [x for x in numbers if x % 2 == 0]
print(another_new_list)

newer_list = [x +1 for x in numbers if x % 2 == 0]
print(newer_list)

name = "Angela"
print(name)
new_list =[letter for letter in name]
print(new_list)
print("".join(new_list))


doubled_num:list = [x*2 for x in range(1,5)]
print(doubled_num)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freedie"]

shorts = [name for name in names if len(name) < 5]
print(shorts)

capital_long_names = [name.upper() for name in names if len(name) > 5]
print(capital_long_names)

list1 = [1,2,3]
list2 = [2,3,4]
result = [number for number in list1 if number in list2]

print(result)

dict_comprehension = {name:random.randint(1,100) for name in names}
print(dict_comprehension)

passed_students = {name: score for (name, score) in dict_comprehension.items() if score > 60}
print(passed_students)
