# Pytanie 6 - jakiej struktury danych użyłbyś do zapisania numerów telefonów
# wszystkich klientów firmy i odpowiadających im nazwisk. Wybierz strukturę tak,
# aby sprawdzenie właściciela numeru telefonu nie zajmowało dużo czasu.

# Następnie stwórz przykładową strukturę przechowującą poniższe informacje:
# 123456789 - Jan Kot
# 999888777 - Anna Lis
# 111222333 - Jan Kot
# Odczytaj nazwisko właściciela numeru 123456789


phone_book = {}

phone_book.update({"Jan Kot" : 123456789})
phone_book.update({"Anna Lis" : 999888777})
phone_book.update({"Jan Kot" : 111222333})
print(phone_book)

# Nie zapisze się pierwszy Jan Kot.
print(phone_book["Anna Lis"])


phone_book = {}

phone_book["Jan Kot"] = [123456789]
phone_book["Anna Lis"] = [999888777]
phone_book["Jan Kot"].append(111222333)
print(phone_book)

print(phone_book["Jan Kot"][0])
# Sprawdzanie elemntu w lisćie to złożoność O(N)
# Sprawdzanie klucza w słowniku lub set to złożonośc O(1) wybieramy słownik

# klucze tel a wartości nazwiska..


phone_book2 = {}

phone_book2[123456789] = "Jan Kot"
phone_book2[999888777] = "Anna Lis"
phone_book2[111222333] = "Jan Kot"
print(phone_book2)

print(phone_book2[123456789])


