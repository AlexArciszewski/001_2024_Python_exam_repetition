# SLOWNIKI

print("Dict czyli słownik")  # klucz : wartość
countries_and_capitals = {"Poland": "Warsaw", "Germany": "Berlin"}
countries_and_capitals['Czechia'] = "Prague"

# wypisanie danych ze słownikach po kluczach
print(countries_and_capitals)
for key in countries_and_capitals.keys():
    print(key)
# wypisanie danych ze słownikach po kluczach i wrzucenie kluczy do listy(mój przykład)

list_countries = []
print(countries_and_capitals)
for key in countries_and_capitals.keys():
    print(key)
    list_countries.append(key)
print(list_countries)
print("checkpoint")

list_cities = []
print(countries_and_capitals)
for capitals in countries_and_capitals.values():
    print(capitals)

for country, capital in countries_and_capitals.items():  # item to klucz plus value?
    print(country + " - ", capital)

print(countries_and_capitals["Poland"])  # jak nie ma klucza to error

print(countries_and_capitals.get("Poland"))  # jak nie ma klucza to wynik to none
print(countries_and_capitals.setdefault("USA","Washington DC"))  # pobiera wartość klucza z wartością a jak go nie ma to bierze to co sie wpisze w nawiasie

print(countries_and_capitals)

print(countries_and_capitals.setdefault("Poland",
                                        "Washington DC"))  # da wynik Warsaw czyli do klucza Poland da wartosc Warsaw

countries_and_capitals["Poland"] = "Cracow"  # zamiana warosci przypisanej do klucza
print(countries_and_capitals)
countries_and_capitals["Poland"] = "Warsaw"
print(countries_and_capitals)
countries_and_capitals.pop("Poland")  # usuwamy wartość to podajemy klucz
print(countries_and_capitals)

print(countries_and_capitals.pop("USA", "Washington DC"))  # wyswietli DC i usunie ale bez USA
print(countries_and_capitals)

print(countries_and_capitals.popitem())  # zwraca usuwa ostatnio dodana wartosc do slownika
print(countries_and_capitals)

if "Germany" in countries_and_capitals.keys():
    print("bingo")
else:
    print("Gone with the wind")

# działa bez .keys()

if "Germany" in countries_and_capitals:
    print("bingo")
else:
    print("Gone with the wind")

# skrócona wersja:
print("Germany" in countries_and_capitals)

countries_and_capitals.clear()
print(countries_and_capitals)

countries_and_capitals2 = {"Poland": "Warsaw", "Germany": "Berlin"}
countries_and_capitals2['Czechia'] = "Prague"
countries_and_capitals2['Sweden'] = "Stockholm"
print(countries_and_capitals2)

blog = {'Website': 'Journaldev', 'tutorial': 'Append to Python dictionary'}
print("Here are the current details: ", blog)

# Adding the author details to the dictionary
blog.update({'Author': 'Pankaj Kumar'})
print("Updated dictionary is: ", blog)

# Appending another dictionary
guests = {'Guest1': 'Meghna'}
blog.update(guests)
print("Updated dictionary is: ", blog)



name_age_dict = {'Toma' : 20, 'Helga' : 19, 'izabela' : 30}

# cały słownik
print(name_age_dict)

#elemnty słownika

print(name_age_dict.items())
# dict_items([('Toma', 20), ('Helga', 19), ('izabela', 30)])

# zawartość słownika po kluczu 'Toma' da wartośc wieku  =20
print(name_age_dict['Toma'])

# zawartość słownika po kluczach 'Toma' da wartości imion
print(name_age_dict.keys())
# zawartość słownika po wartosciach 'Toma' da wartości lat
print(name_age_dict.values())

# update słwonika o nowe dane. Dane trafiaja na koniec
name_age_dict.update({'Ala' : 33})
print(name_age_dict)

name_age_dict.update({'Kacper' : 33, 'Nina' : 10})
print(name_age_dict)

#pobranie po kluczu imienia
print(name_age_dict.get('Kacper'))
print(name_age_dict.get())

#zwracanie sumy elementów dict
pensje = {'ksiegowa': 5000, 'kierowca': 4500, 'recepcjonistka': 4000}
print(sum(pensje.values()))



#usuwanie del
Members = {"John": "Male", "Kat": "Female", "Doe": "Female", "Clinton": "Male"}

del Members["Doe"]
print(Members)
# {"John": "Male", "Kat": "Female", "Clinton": "Male"}


#Zagnieżdżanie danych:
przepis = {
    'nalesniki': ['jaja', 'maka', 'sol', 'mleko', 'dzem'],
    'kanapki z serem' : ['chleb pelnoziarnisty', 'ser zołty', 'maslo', 'pomidor']
}

x = przepis.get('nalesniki')[0]
print(x)



# Tworzenie menu z użyciem dict'a

def menu():
    print("menu")


def add_to_list():
    print("dodaje do listy")


def remove_from_list():
    print("Usuwam z listy")


from typing import Callable

def menu():
    print("To jest menu.")

def add_to_list():
    print("Dodano do listy.")

def remove_from_list():
    print("Usunięto z listy.")

options: dict[int, Callable] = {
    1: menu,
    2: add_to_list,
    3: remove_from_list,
}

user_choice = int(input("Podaj swój wybór: "))

if user_choice in options:
    options[user_choice]()  # wywołanie funkcji
else:
    print("Nieprawidłowy wybór.")



dict.clear()	#Usuwa wszystkie elementy ze słownika
dict.copy()	#Zwraca płytką kopię słownika
dict.fromkeys(seq[value])	#Tworzy nowy słownik z kluczami z seq i wspólną wartością value
dict.get(key[default])	#Zwraca wartość dla klucza key, lub default, jeśli klucza nie ma
dict.items()	#Zwraca widok (iterowalny) par (klucz, wartość)
dict.keys()	#Zwraca widok (iterowalny) wszystkich kluczy
dict.pop(key[default])	#Usuwa i zwraca wartość podanym kluczu; jeśli brak – zwraca default lub błąd
dict.popitem()	#Usuwa i zwraca losową (w Pythonie 3.6+ ostatnią) parę (klucz, wartość)
dict.setdefault(key[default])	#Zwraca wartość pod key, jeśli nie istnieje – tworzy go z default
dict.update([other])#	Dodaje/aktualizuje pary klucz-wartość z innego słownika lub iterowalnego
dict.values()	#Zwraca widok (iterowalny) #wszystkich wartości






# Zad 13.
# Utwórz słownik, który przechowuje definicje wyrazów i ich wytłumaczenia.
# Zarządzanie słownikiem ma się odbywać za pomocą interaktywnego
# MENU (MENU ma być obsługiwane za pomocą print() oraz input() oraz ma wyglądać tak jak poniżej):
# 1. Dodaj słowo wraz z definicją
# 2. Znajdź definicję słowa
# 3. Usuń słowo wraz z definicją z słownika
# 4. Zakończ program
#
import sys
start_message = """ Choose option     
    1. Add a word along with its definition
    2. Find the definition of a word
    3. Remove a word along with its definition from the dictionary
    4. End the program   """

program_running = True
if program_running == False:
    sys.exit(1)





while program_running == True:
    number = int(input(f"hello, {start_message} "))
    if number == 1:
        dict_words = {}
        a = input("pls give me the word: ")
        b = input(f"pls give me the meaning of {a} word: ")
        c = {a : b}
        dict_words.update(c)
        print(c)
    elif number == 2:
        y = input("Find the word u wanna check: ")
        for key in dict_words.keys():
            if key == y:
                print(dict_words[key])

    elif number == 3:
        z = input("Pls give me the word U wanna delete; ")
        # for key in dict_words.keys():     to źle bonie można usuwac el ze słownika po którym się iteruje
        #     if key == z:
        if z in dict_words.keys():
            dict_words.pop(z)
        print(f"word was successfully deleted")
        print(dict_words)

        pass
    elif number == 4:
        print("program will now exit....")
        program_running = False
        pass
    else:
        print(f"Something went wrong")

#clear wszystkie el. ze słownika:

countries={"Ghana": "Accra", "China": "Beijing"}
# using the del keyword
del countries["China"]
print(countries)

#del usuwa ze słownika wybrany element:

countries={"Ghana": "Accra", "China": "Beijing"}
# using the del keyword
del countries["China"]
print(countries)


#pop usuwa element ze słownika
countries={"Ghana": "Accra", "China": "Beijing"}
# using the pop() method
countries.pop("China")
print(countries)

#popitem metoda usuwa ostatni dodany el ze słownika:
countries={"Ghana": "Accra", "China": "Beijing"}
# using the clear() method
countries.popitem()
print(countries)

# Zad 2.
# Zmodyfikuj kod z zadania 1 tak, aby możliwe było dodawanie i usuwanie przez użytkownika informacji o
# nowych albumach do słownika. Program ma zawierać proste menu.
from typing import Callable


dict_of_albums = {
                    'The Sensual World' : 'Kate Bush',
                    'Shaday' : 'Ofra Haza',
                    'Achtung Baby' : 'U2',
                    'Aion' : 'Dead Can Dance',
                    'Invisible Touch' : 'Genesis'
                }

def menu():
    print("             MENU")
    print("1 Add album to the database")
    print("2 Remove album from the database")
    print("3 Check all the albums in the database")
    print("4 Find the album in the database")
    print("5 Exit the program")


def add_album():
    print("Adding new band  & album ...")
    album = input("Pls give me the name of the album U wanna add: ")
    band = input("Pls give me the name of the band U wanna add: ")
    dict_of_albums.update({album: band})
    print(f"The final result is {dict_of_albums}")
    menu()
def remove_album():
    album = input("Pls give me the name of the album U wanna delete: ")
    band = input("Pls give me the name of the band U wanna delete: ")
    if album in dict_of_albums.keys():
        del dict_of_albums[album]
        print(dict_of_albums)
        menu()


def check_albums():
    print(dict_of_albums)

def find_album():
    album = input("Pls give me the name of the album U wanna find: ")
    if album in dict_of_albums.keys():
        print(album, dict_of_albums[album])
        menu()

def exit_the_program():
     print("Bye")

def run_program():
    options: dict[int, Callable] ={
        1: add_album,
        2: remove_album,
        3: check_albums,
        4: find_album,
        5: exit_the_program
    }
    while True:
        menu()
        # dict_word()
        choice = int(input("Enter your choice: "))

        if choice == 5:
            print("Exiting...")
            exit_the_program()
            break
        elif choice in options:
            options[choice]()
        else:
            print("Invalid choice. Please try again.")


#Tworzenie dict z list:

# #Dict z list
# dict_of_words = dict(zip(list_of_words, list_of_reps))
# print(dict_of_words)
#
#
# dict2_of_words = {}
#
# for i in range(len(list_of_words)):
#     dict2_of_words[list_of_words[i]] = list_of_reps[i]
# print(dict2_of_words)

#Scalanie słowników
lovers = {1: 'Rahima', 2: 'Alishba', 3: 'Fizza'}
friends = {4: 'Bilal', 5: 'Arbab', 6: 'Shahzor'}


lovers.update(friends)
print(lovers)

zamowienia = {
    "Klient_1335" : {"nazwa_potrawy" : "rosół", "ocena" : 5, "rachunek" : 20.0},
    "Klient_222" : {"nazwa_deseru" : "lody waniliowe", "rachunek" : 5.0 }
    }

print(zamowienia)

for klient in zamowienia:
    print(klient)
    for order in zamowienia[klient]:
        print(order,zamowienia[klient][order])

# Klient_1335
# nazwa_potrawy rosół
# ocena 5
# rachunek 20.0
# Klient_222
# nazwa_deseru lody waniliowe
# rachunek 5.0



some_cars = {"1994 Dodge Viper" : 1, "1968 Ford Mustang Fastback" : 2, "1998 Hummer H1" : 3 }

for cars in some_cars:
    print(some_cars)


print(some_cars.values())
print(some_cars.keys())
print(some_cars["1994 Dodge Viper" ])
#1

for key, value in some_cars.items():
    if value == 1:
        print(key)
#"1994 Dodge Viper"
for key, value in some_cars.items():
    if key == "1994 Dodge Viper" :
        print(value)
#1
def get_key_by_value(dict, val):
    return [k for k, v in dict.items() if v == val]
#"1994 Dodge Viper"
print(get_key_by_value(some_cars, 1))  # ['1994 Dodge Viper']

cities = ['Boston', 'Londyn', 'Boston', '']
temperatures = ['12', '10', '12', '']

cities_temps = dict(zip(cities, temperatures))
print(cities_temps)


# for key in cities_temps.copy().keys():
#      if cities_temps.copy().keys() == '' or ' ':
#          cities_temps.pop(key)
# print(cities_temps)

for key, value in list(cities_temps.items()):
    if value == '':
        del cities_temps[key]
print(cities_temps)









#podmiana elementów w dick el z listy

dct = {'Tom': 0, 'Clare': 0, 'Rich': 0, 'Rosie': 0}
lst = [21.95, 20.9, 20.9, 18.65]



i = 0
for key in dct.keys():
    dct[key] = lst[0]

    i += 1

print(dct)


dct = {'Tom': 0, 'Clare': 0, 'Rich': 0, 'Rosie': 0}
lst = [21.95, 20.9, 20.9, 18.65]

for key, val in zip(dct.keys(), lst):
    dct[key] = val


print(dct)



#podmiana elementów s słowników elemetami z listy:

dct = {'Tom': 0, 'Clare': 0, 'Rich': 0, 'Rosie': 0}
lst = [21.95, 20.9, 20.9, 18.65]

for key, val in zip(dct.keys(), lst):
    dct[key] = val


print(dct)

#Odwracanie slownika:
some_dict = {'a' : 3, 'b' : 1, 'c' : 10, 'd' : 15, 'e' : 20}
print(some_dict)
print(some_dict.keys())
print(some_dict.values())

new_keys = some_dict.values()
new_values = some_dict.keys()
converted_dict = dict(zip(new_keys, new_values))
print(converted_dict)

print("opcja B")

odwrocony_d = {}
for key, value in some_dict.items():
    odwrocony_d[value] = key
print(odwrocony_d)

#max wartości;
# Przykładowy słownik
my_dict = {'Alice': 50, 'Bob': 75, 'Charlie': 100}

# Wyciąganie klucza z najwyższą wartością
max_key = max(my_dict, key=my_dict.get)

print(f"Klucz z najwyższą wartością to: {max_key}")
print(f"Najwyższa wartość to: {my_dict[max_key]}")


max_bid:float = max(bid_dict.values())
        winner:str = None
        for key, value in bid_dict.items():
            if value == max_bid:
                winner = key
                break
        print(f"Auction ended . The winner was: {key}")