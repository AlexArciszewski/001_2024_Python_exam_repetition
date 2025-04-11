# Zad 5.
# Program ma tworzyć rachunek za prestiżową kolację w restauracji dla poszczególnych osób.
#
# Dla przykładowej listy:
#
# bill_items = [
#     ['Tom', 'Calamari', 6.00],
#     ['Tom', 'American Hot', 11.50],
#     ['Tom', 'Chocolate Fudge Cake', 4.45],
#     ['Clare', 'Bruschetta Originale', 5.35],
#     ['Clare', 'Fiorentina', 10.65],
#     ['Clare', 'Tiramisu', 4.90],
#     ['Rich', 'Bruschetta Originale', 5.35],
#     ['Rich', 'La Reine', 10.65],
#     ['Rich', 'Honeycomb Cream Slice', 4.90],
#     ['Rosie', 'Garlic Bread', 4.35],
#     ['Rosie', 'Veneziana', 9.40],
#     ['Rosie', 'Tiramisu', 4.90],
# ]
#
# Wynikiem ma być słownik w postaci:
# {
# ‘Tom’ : {‘potrawy’ : [‘Calamari’, ‘American Hot’, ‘Chocolate Fudge Cake’], ‘cena’ : 21.95},
# ‘Clare’ : {‘potrawy : [‘Bruschetta Originale‘, ‘Fiorentina’, ‘Tiramisu’], ‘cena’ : 20.90},
# …
# }


bill_items = [
    ['Tom', 'Calamari', 6.00],
    ['Tom', 'American Hot', 11.50],
    ['Tom', 'Chocolate Fudge Cake', 4.45],
    ['Clare', 'Bruschetta Originale', 5.35],
    ['Clare', 'Fiorentina', 10.65],
    ['Clare', 'Tiramisu', 4.90],
    ['Rich', 'Bruschetta Originale', 5.35],
    ['Rich', 'La Reine', 10.65],
    ['Rich', 'Honeycomb Cream Slice', 4.90],
    ['Rosie', 'Garlic Bread', 4.35],
    ['Rosie', 'Veneziana', 9.40],
    ['Rosie', 'Tiramisu', 4.90],
]

ppl_dish = {}
ppl_list = []
name_list =[]
dish_list =[]
total_price =[]
for ppl_list in bill_items:
    name_list.append(ppl_list[0])
    dish_list.append(ppl_list[1])
    total_price.append(ppl_list[2])
print(dish_list, name_list, total_price)

dish_list_1 = dish_list[0:3]
dish_list_2 = dish_list[3:6]
dish_list_3 = dish_list[6:9]
dish_list_4 = dish_list[9:12]









#
# for ppl_list in bill_items:
#     print(ppl_list)
# #names as keys
# names = []
# for ppl_list in bill_items:
#     names.append(ppl_list[0])
# #print(names)
# names_set = set(list(names))
# names_upd_list = list(names_set)
# print(names_upd_list)


# rain = {}
#
# while True:
#     data = input(": ")
#
#     if data == "":
#         break
#
#     city, raining = data.split()
#     raining = int(raining)
#
#     if city in rain:
#         rain[city] += raining
#     else:
#         rain[city] = raining
#
# for city, raining in rain.items():
#     print(f"{city} - {raining}")
















