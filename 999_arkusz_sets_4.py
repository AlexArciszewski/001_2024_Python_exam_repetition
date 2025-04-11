# Zad 3.
# Mając poniższy słownik:
# {‘a’ : 3, ‘b’ : 1, ‘c’ : 10, ‘d’ : 15, ‘e’ : 20}
# dokonaj jego odwrócenia, tzn. niech wartości staną się kluczami, a klucze wartościami.
# Dla powyższego przykładu poprawnym wynikiem będzie:
# {3 : ‘a’, 1 : ‘b’, 10 : ‘c’, 15 : ‘d’, 20 : ‘e’}


some_dict = {'a' : 3, 'b' : 1, 'c' : 10, 'd' : 15, 'e' : 20}
print(some_dict)
print(some_dict.keys())
print(some_dict.values())

new_keys = some_dict.values()
new_values = some_dict.keys()
converted_dict = dict(zip(new_keys, new_values))
print(converted_dict)

print("opcja B")

odwrocony_d = {}
for key, value in some_dict.items():
    odwrocony_d[value] = key
print(odwrocony_d)




rain = {}

while True:
    data = input(": ")

    if data == "":
        break

    city, raining = data.split()
    raining = int(raining)

    if city in rain:
        rain[city] += raining
    else:
        rain[city] = raining

for city, raining in rain.items():
    print(f"{city} - {raining}")
