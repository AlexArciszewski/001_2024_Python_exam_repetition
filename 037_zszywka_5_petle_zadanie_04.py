# Zad. 4
# Napisz program, wyświetlający n kolejnych potęg liczby 2. Wartość n podaje użytkownik.

exp = []
list_numbers =[]

number = int(input("number pls: "))

for i in range(0, number + 1):
    exp.append(i)

for el in exp:
    list_numbers.append(2**el)
# print(list_numbers)

for num in list_numbers:
    print(num)


