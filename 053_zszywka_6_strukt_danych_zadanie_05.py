# Zad 5.
# Wprowadź krotkę d = (1, [2, 4], 'tekst', 3 + 5j) i:
# a) wyświetl jej ostatni element
# b) wyświetl jej pierwszy i drugi element
# c) sprawdź, czy tekst 'abc' jest elementem krotki


d = (1, [2, 4], 'tekst', 3 + 5j)
print(d[-1])
print(d[0:2])

for element in d:
    if element == 'abc':
        print(True)
    else:
        print(False)
