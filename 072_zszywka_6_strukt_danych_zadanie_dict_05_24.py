# Zad5
# Napisz skrypt, który wygeneruje i wyprintuje słownik zawierający liczby pomiędzy
# (1 - n; n jest liczbą podawaną przez użytkownika) w formie (x, x*x).
# Przykładowy input: n = 5
# Oczekiwany wynik: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n = int(input("number pls: "))
dict_of_numbers = {}
keys = []
values = []
for i in range(1, n+1):
    keys.append(i)
    values.append(i**2)
dict_of_numbers = dict(zip(keys, values))
print(dict_of_numbers)




