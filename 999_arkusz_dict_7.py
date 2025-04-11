# Wyboraź sobie, że otrzymałeś z API następujące dane:

data_dict = {
    'data': [1, 2, 'asd', [2, 3, 4, 5]],
    'nested_analysis': {
        'analysis_1': [1, 10, 15, 120.2, '120'],
        'analysis_2': [10, 100, 'test', 200, 300]
    },
    'probes': [['probe_1', 'probe_2'], 'probe_3']
}
# Twoim zadaniem jest wyłuskanie spod każdego klucza w powyższym słowniku tylko tych danych, które są typu str i wyświetlić je na ekranie.

print(data_dict)
print(data_dict.values())
print('zaw listy')
print((data_dict['data'])[2])
print(f"first string is: {(data_dict['data'])[2]}")
print(data_dict['nested_analysis'])
print(data_dict['nested_analysis']['analysis_2'][2])
print(f"second string is: {data_dict['nested_analysis']['analysis_2'][2]}")
print(data_dict['probes'][0][0], data_dict['probes'][0][1],data_dict['probes'][1])
print(f"third strings are:{data_dict['probes'][0][0]}, {data_dict['probes'][0][1]},{data_dict['probes'][1]}")



# names = {
#     "Michu" : "Dawaj hajs",
#     "Toma": "Oma",
#     }
#
# name = input(": ")
#
# if name in names.keys():
#     print(names[name])

new_str = ""
# some_text = input(": ")
some_text = "Ala ma pod kota ?"
bad_el = [",", ".", ":", ";", ",", "!", "?"]
for char in some_text:
    if char not in bad_el:
        new_str += char

print(new_str)
new_list =[]
new_list = new_str.split(" ")
print(new_list)
empty = ""
for el in new_list[:]:
    if el == empty:
        new_list.remove(empty)
print(new_list)

print(len(new_list))
for el in new_list:
    if el == el.capitalize():
        print(f"There is a capitalized word {el} ")

for el2 in new_list:
    if el2 != el2.capitalize():
        print(f"There is no capitalized word {el2} ")

forbidden= ["i", "w", "na", "pod", "dla"]
found = False
for el3 in forbidden:
    if el3 in new_list:
        word_index = []
        for i in range(len(new_list)):
            if new_list[i] == el3:
                word_index.append(i)
        print(f"{el3}, {word_index}")
        znaleziono = True
print(new_list)
print(sorted(new_list))


for i in range(5):
    print("*" + i*"*")

for i in range(4):
    print("***")

for i in range(1, 5 + 1, 2):
    spacje = ' ' * ((5 - i) // 2)
    gwiazdki = '*' * i
    print(spacje + gwiazdki)

# Rysowanie pnia
spacje = ' ' * ((5 - 1) // 2)
print(spacje + '*')



owoce = ['jabłko', 'banan', 'wiśnia']

for indeks, owoc in enumerate(owoce):
    print(f"{indeks}: {owoc}")










































