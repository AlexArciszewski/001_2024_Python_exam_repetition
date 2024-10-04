# Pytanie 10 - korzystając ze słownika stworzonego w poprzednim zadaniu
# sprawdź czy któraś z liter wystąpiła w stringu dokładnie 4 razy.
# Jeśli tak - wypisz True, jeśli nie - False.

litery = {'m': 1, 'y': 3, 's': 1, 'z': 3, 'd': 2, 'o': 2, \
          'k': 2, 'a': 2, 'u': 2, 'j': 2, 'ą': 2, 'g': 1, \
          't': 1, 'n': 1, 'i': 1, 'e': 1, 'c': 1}


for letter, value in litery.items():
    if value == 4:
        print(True)
    else:
        print(False)

print("Opcja B")

print(True if 4 in litery.values() else False)

print("Opcja C")
print(litery.values())



for value in litery.values():
    if value == 4:
        print(True)
    else:
        print(False)
