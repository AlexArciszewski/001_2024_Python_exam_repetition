# Zad. 5
# Napisz program, który wyświetli liczby z przedziału <50; 100> podzielne przez całkowitą liczbę k,
# którą podaje użytkownik. Przekształć program tak, aby przedział podawał również użytkownik.




s = int(input(" Pls give starting number: "))
e = int(input(" Pls give ending number: "))
k = int(input(" pls give me the divisor: "))
number_range = []

for i in range(s, e+1):
    number_range.append(i)
print(f" The list of numbers is {number_range}")

for number in number_range:
    if number % k == 0:
        print(number)


