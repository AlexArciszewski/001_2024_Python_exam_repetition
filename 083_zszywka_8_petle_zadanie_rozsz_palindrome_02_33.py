# Zad 2.
# Napisz program, sprawdzający czy dany wyraz jest palindromem
# (jest czytany tak samo od przodu i tyłu), np. sedes, Anna.


word = input("Give me some word: ")

if word == word[::-1]:
    print(True)
else:
    print(False)

