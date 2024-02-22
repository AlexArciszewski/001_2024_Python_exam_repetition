# Zad 4.
# Napisz program, który utworzy dwa zbiory:
# ●	zbiór A: liczb naturalnych parzystych mniejszych od n (n podaje użytkownik)
# ●	zbiór B: liczb naturalnych mniejszych od n, które przy dzieleniu przez 3 dają resztę
#     2 oraz zbiory będące wynikiem następujących operacji matematycznych:
#
#
# C = A + B, D = A & B, E = A – B, F = B ^ A (różnica symetryczna)
#
#
#
# Dla każdego z utworzonych zbiorów program poda informacje o jego nazwie,
# liczebności i zawartych w nim elementach. Na koniec program sprawdzi,
# czy zbiór B zawiera się w zbiorze A.


chosen_number = int(input("number pls: "))

list_of_natural_even_num = []
list_of_natural_not_even_num = []


# zbiór A: liczb naturalnych parzystych mniejszych od n (n podaje użytkownik)
for number in range(2, chosen_number):
    if number % 2 == 0:
        list_of_natural_even_num.append(number)
print(list_of_natural_even_num)
set_of_natural_even_num = set(list_of_natural_even_num)

# zbiór B: liczb naturalnych mniejszych od n, które przy dzieleniu przez 3 dają resztę
#     2 oraz zbiory będące wynikiem następujących operacji matematycznych:

for number2 in range(2, chosen_number):
    if number2 % 3 == 2:
        list_of_natural_not_even_num.append(number2)
print(list_of_natural_not_even_num)
set_of_natural_not_even_num = set(list_of_natural_not_even_num)


# C = A + B suma
C = set_of_natural_even_num.union(set_of_natural_not_even_num)
print(C)

# D = A & B cz. wsp.
D = set_of_natural_even_num & set_of_natural_not_even_num
print(D)

# E = A – B te co w A po odjęciu tych co w B
E = set_of_natural_even_num - set_of_natural_not_even_num
print(E)

# F = B ^ A (różnica symetryczna)
F = set_of_natural_not_even_num ^ set_of_natural_even_num
print(F)