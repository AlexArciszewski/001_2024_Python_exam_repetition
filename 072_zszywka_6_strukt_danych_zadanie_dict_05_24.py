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


lovers = {1: 'Rahima', 2: 'Alishba', 3: 'Fizza'}
friends = {4: 'Bilal', 5: 'Arbab', 6: 'Shahzor'}

lovers.update(friends)
print(lovers)

data_dict = { "V":"S001", "VI": "S002", "VII": "S001", "VIII": "S005", "IX":"S005", "X":"S009", "XI":"S007" }

data_values = []

for key in data_dict:
    if data_dict[key] not in data_values:
        data_values.append(data_dict[key])
    elif data_dict[key] in data_values:
        data_values.remove(data_dict[key])
print(data_values)



