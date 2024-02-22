# Zad 8.
# Napisz program, który wydrukuje wszystkie unikalne wartości ze słownika.
# Dla danych:
{ "V":"S001", "VI": "S002", "VII": "S001", "VIII": "S005", "IX":"S005", "X":"S009", "XI":"S007" }
# Oczekujemy wyniku:
# “S002”, “S009”, “S007”

some_dict =  {
    "V":"S001",
    "VI": "S002",
    "VII": "S001",
    "VIII": "S005",
    "IX":"S005",
    "X":"S009",
    "XI":"S007"
    }
print(some_dict)

list_of_values = []
unique_val = []
for key in some_dict:
    if some_dict[key] not in list_of_values:
        list_of_values.append(some_dict[key])
    elif some_dict[key] in list_of_values:
        list_of_values.remove(some_dict[key])



print(list_of_values)
# ['S001', 'S002', 'S001', 'S005', 'S005', 'S009', 'S007']
#   0       1       2       3       4       5       6










