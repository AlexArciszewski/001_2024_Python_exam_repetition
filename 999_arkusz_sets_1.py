# Zad 1.
# Utwórz listę składającą się z następujących elementów: 'zielony', 'czerwony', 'niebieski', 'czarny', 'fioletowy',
# 'granatowy', 'niebieski', 'czarny', 'czarny', 'zielony', 'cytrynowy', 'granatowy', 'niebieski', 'indygo', 'zielony',
# 'czerwony'.
# Przekształć tę listę w zbiór i zachowaj pod nową nazwą, a następnie:
# –	policz, ile elementów zawiera oryginalna lista kolorów
# –	policz, ile różnych kolorów zostało użytych
# –	wyświetl każdy z elementów zbioru w oddzielnej linii
# –	dodaj do zbioru nazwę jakiegoś innego koloru (sprawdź efekt przez wyświetlenie zawartości)
# –	usuń ze zbioru jakiś kolor (ponownie sprawdź efekt)

color_list = [
    'zielony', 'czerwony', 'niebieski', 'czarny', 'fioletowy',
    'granatowy', 'niebieski', 'czarny', 'czarny', 'zielony',
    'cytrynowy', 'granatowy', 'niebieski', 'indygo', 'zielony',
    'czerwony'
    ]
print(color_list)
color_set = set(color_list)
print(color_set)
print(len(color_set))
print(len(color_list))
color_order = list(color_set)
print(len(color_order))
for color in color_set:
    print(color)
color_set.add('amieliniowy')
print(color_set)
color_set.discard('amieliniowy')
print(color_set)



#text = input('text: ')
text = "Ala ma kota Ala ; : ,  ? ."

to_remove = [",", ".", ":", ";", "!", "?"]
new_string = ""
for char in text:
    if char not in to_remove:
        new_string += char
print(new_string)

list_new_string = new_string.split(" ")
print(list_new_string)
list_newer_string = []
for word in list_new_string:
    if word != "":
        list_newer_string.append(word)
print(list_newer_string)

word_tuple = tuple(list_newer_string)
print(len(word_tuple))

word_sentence = " ".join(word_tuple)
print(word_sentence)
print(word_tuple[0], word_tuple[-1])

#sets
print(list_newer_string)
set_text = set(list_newer_string)
print(len(set_text))
unique_text = " ".join(set_text)
print(unique_text)
print('set el')
print(set_text)
#ostatni element zbioru
for element in set_text:
    last = element
print(element)


#pierwszy z konwersją do listy

first_el = (list(set_text))[0]
print(first_el)















