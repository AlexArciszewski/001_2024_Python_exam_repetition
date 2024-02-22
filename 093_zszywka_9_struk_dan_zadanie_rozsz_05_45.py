# Zad 5.
# Program ma tworzyć rachunek za prestiżową kolację w restauracji dla poszczególnych osób.
#
# Dla przykładowej listy:

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
toms_dishes = []
toms_cost = []


for dish in bill_items:
    if dish[0] == 'Tom':
        toms_dishes.append(dish[1])
        toms_cost.append(dish[2])
tom_cost_sum = sum(toms_cost)
print(toms_dishes, toms_cost, tom_cost_sum)


clare_dishes = []
clare_cost = []

for dish in bill_items:
    if dish[0] == 'Clare':
        clare_dishes.append(dish[1])
        clare_cost.append(dish[2])
clare_cost_sum = sum(clare_cost)
print(clare_dishes, clare_cost, clare_cost_sum)

rich_dishes = []
rich_cost = []

for dish in bill_items:
    if dish[0] == 'Rich':
        rich_dishes.append(dish[1])
        rich_cost.append(dish[2])
rich_cost_sum = sum(rich_cost)
print(rich_dishes, rich_cost, rich_cost_sum)


rosie_dishes = []
rosie_cost = []

for dish in bill_items:
    if dish[0] == 'Rosie':
        rosie_dishes.append(dish[1])
        rosie_cost.append(dish[2])
rosie_cost_sum = sum(rosie_cost)
print(rosie_dishes, rosie_cost, rosie_cost_sum)






list_name = []
starting_cost = []

for dish in bill_items:
    name = str(dish[0])
    list_name.append(name)
    starting_cost.append(0)


final_cost = [tom_cost_sum, clare_cost_sum, rich_cost_sum, rosie_cost_sum]
print(final_cost)
print(list_name)
print(starting_cost)




dict_names_at_start = dict(zip(list_name, starting_cost))
print(dict_names_at_start)





