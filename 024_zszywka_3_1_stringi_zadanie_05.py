# Zad5
# Pobierz od użytkownika dowolny napis zawierający 5 białych znaków (spacji) na początku, a następnie:
# ▪ wyświetl ten napis
# ▪ usuń wiodące białe znaki i wyświetl napis po tej zmianie



word = input("pls give me some text: ")
word = "     " + word
print(word)
print(word.lstrip())
