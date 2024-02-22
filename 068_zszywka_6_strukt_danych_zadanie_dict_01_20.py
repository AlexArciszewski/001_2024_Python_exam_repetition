# Zad 1.
# Wprowadź poniższy słownik do programu. Program ma działać, tak jak poniżej:
# • wyświetla wszystkie klucze na konsoli (tzn. nazwy wszystkich albumów),
# • pobiera od użytkownika łańcuch i sprawdza czy odpowiada on kluczowi ze słownika.
# Jeśli tak, to wyświetlany jest odpowiedni komunikat, np.: "Wykonawcą albumu "Achtung baby" jest “U2".
# W przeciwnym razie wyświetlany jest komunikat: "Brak danych".

dict_of_albums = {
                    'The Sensual World' : 'Kate Bush',
                    'Shaday' : 'Ofra Haza',
                    'Achtung Baby' : 'U2',
                    'Aion' : 'Dead Can Dance',
                    'Invisible Touch' : 'Genesis'
                }
print(dict_of_albums)
# • wyświetla wszystkie klucze na konsoli (tzn. nazwy wszystkich albumów),

for album in dict_of_albums:
    print(album)

# • pobiera od użytkownika łańcuch i sprawdza czy odpowiada on kluczowi ze słownika.

name_of_album = input("Pls give me the name of the album to check: ")
if name_of_album in dict_of_albums.keys():
    print(f"The name of the band is: {dict_of_albums[name_of_album]} ")
else:
    print("No such a band in the database: ")


# #  To nie działa
# name_of_album = input("Pls give me the name of the album to check: ")
# if name_of_album in album:
#     print(f"The name of the band is: {dict_of_albums[album]}")
# else:
#     print("No such a band in the database: ")