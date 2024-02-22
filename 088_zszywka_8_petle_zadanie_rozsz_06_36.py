# Zad 6.
# Stwórz program, który policzy częstotliwość cyfr w danej liczbie (którą poda użytkownik).
# Przykład:
# Input: 1235555
# Output:
# 1: 1
# 2: 1
# 3: 1
# 5: 4
#
# Podpowiedź:
# Aby łatwo przechodzić po wszystkich cyfrach w liczbie, przekonwertuj ją na typ str.
# Częstotliwość występowania danych cyfr możesz przechowywać wewnątrz słownika.


number = int(input("number?: "))
number_str = str(number)
number_dict = {}
len = len(number_str)
print(f"The chosen number: {number} has {len} digits")

number_list = []
for digit in number_str:
    print(digit)
    number_list.append(digit)
print(number_list)
reps_list = []

for el in number_list:
    print(el, number_list.count(el))
    dict_key = el
    dict_value = (number_list.count(el))
    data = {dict_key: dict_value}
    number_dict.update(data)
# dict_key = el
# dict_value = (number_list.count(el))
# data = {dict_key: dict_value }
#
# number_dict.update(data)

print(number_dict)










