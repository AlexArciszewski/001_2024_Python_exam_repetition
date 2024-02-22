# Zad 1.
# Utwórz listę składającą się z następujących elementów:
# 'zielony', 'czerwony', 'niebieski', 'czarny', 'fioletowy', 'granatowy', 'niebieski', 'czarny', 'czarny', 'zielony', 'cytrynowy', 'granatowy', 'niebieski', 'indygo', 'zielony', 'czerwony'.
# Przekształć tę listę w zbiór i zachowaj pod nową nazwą, a następnie:
# –	policz, ile elementów zawiera oryginalna lista kolorów
# –	policz, ile różnych kolorów zostało użytych
# –	wyświetl każdy z elementów zbioru w oddzielnej linii
# –	dodaj do zbioru nazwę jakiegoś innego koloru (sprawdź efekt przez wyświetlenie zawartości)
# –	usuń ze zbioru jakiś kolor (ponownie sprawdź efekt)

colors = ['zielony', 'czerwony', 'niebieski', 'czarny', 'fioletowy', 'granatowy', 'niebieski', 'czarny', 'czarny', 'zielony', 'cytrynowy', 'granatowy', 'niebieski', 'indygo', 'zielony', 'czerwony']

# Stworzenie set'a
set_of_colors = set()
for color in colors:
    set_of_colors.add(color)

print(set_of_colors)

# policz, ile elementów zawiera oryginalna lista kolorów
print(len(set_of_colors))

# policz, ile różnych kolorów zostało użytych
print(len(colors))

# wyświetl każdy z elementów zbioru w oddzielnej linii
for el in set_of_colors:
    print(el)

# dodaj do zbioru nazwę jakiegoś innego koloru (sprawdź efekt przez wyświetlenie zawartości)

print(set_of_colors)

new_color = "zolty"
if new_color not in set_of_colors:
    set_of_colors.add(new_color)

print(set_of_colors)

# usuń ze zbioru jakiś kolor (ponownie sprawdź efekt)

set_of_colors.discard("zolty")
print(set_of_colors)