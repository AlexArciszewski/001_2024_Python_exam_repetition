# Pytanie 5 - z poniższej listy wypisz stringa "schowany"

list_struct = [[34, False], [0], [('abc', 123), {'a': 1, 'x': (True, 'schowany', 5)}]]

for list in list_struct:
    print(list)
outer_list = list_struct[2]
print(outer_list[1])
inner_dict = outer_list[1]

for key in inner_dict:
    print(key)

value = inner_dict['x']
print(value)
print((value)[1])



print(list_struct[2][1]['x'][1])