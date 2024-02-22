def give_me_your_name(name, surname): #funkcja ma 2 parametry
    print("Welcome", name, surname)

#argumenty funkcji
name = input("name pls: ")
surname = input("surname pls: ")

give_me_your_name(name, surname)


print("Option no. 2")

name = input("name pls: ")
surname = input("surname pls: ")

give_me_your_name(name, surname)

# Argumenty funkcji - i tutaj uważaj, aby nie zostać zmylonym! Formalnie ujmując,
# parametr funkcji to nie to samo, co jej argument.
# Parametry bowiem deklarujemy zaraz po nazwie funkcji, a argumenty to już konkretne wartości,
# które przekazujemy do funkcji w momencie jej wywołania!
# Ciało funkcji – umieszczamy w niej to, co ma zostać wykonane w ramach danej funkcji,
# pamiętać należy o wcięciu poprzedzającym każdą linijkę ciała.

print("Another way")

def give_me_our_name_key_arg(greeting, name1, surname1, text):
    print(f"{greeting},{name1}, {surname1}, {text}")

give_me_our_name_key_arg("Hello", "Jack", "Rabbit Slim","This is your contest")
# Hello,Jack, Rabbit Slim, This is your contest

print("Keyword arguments argumenty nazwane")
def using_key_words(greetings, name2, surname2, Text2):
    print(f"{greetings},{name2}, {surname2}, {Text2}")

using_key_words(greetings = "Hi There", name2 = "Ala", surname2 ="Makota", Text2 = "Ihaaa")
# Hi There,Ala, Makota, Ihaaa
#niezależnie od kolejności będzie to samo wyświetlane
using_key_words(name2 = "Ala", surname2 ="Makota", Text2 = "Ihaaa", greetings = "Hi There")
# Hi There,Ala, Makota, Ihaaa


print("argumenty domyslne")

def powitaj(powitanie, imie="Jan", wiek=10, narodowsc ="Polska"):
    print(f"{powitanie}, {imie}. Masz {wiek} lat. Jestes narodowosci:{narodowsc}")
# Hi There,Ala, Makota, Ihaaa
# Hi There,Ala, Makota, Ihaaa

powitaj(powitanie="Hej")
powitaj(powitanie="Witaj")

# Hej, Jan. Masz 10 lat. Jestes narodowosci:Polska
# Witaj, Jan. Masz 10 lat. Jestes narodowosci:Polska


print("*args and **kwargs")

print("*args")
print("Funkcja, która będzie obliczała sumę wszystkich wysłanych do niej argumentów.")


def sum_numbers(*args):
    sum = 0
    for num in args:    #*args to obiekt, po którym możemy iterować, ale nie możemy zmieniać jego zawartości na poziomie funkcji.
        sum += num

    return sum

print(sum_numbers(1, 2, 3))
# 6

def show_arguments(*args):
    print(*args)
    print(args[0])
    print(args[-1])

print(show_arguments(1, 2, 3, 4, 5))
#1 2 3 4 5
# 1
# 5
# None
2
def show_arguments(*args):
     return args


print(show_arguments(1, 2, 3, 4, 5))

# (1,2,3,4,5

def show_band(**kwargs):
    print(kwargs["PO"]) #pojedyncze odwolanie do klucza
    for key in kwargs:
        print(f"{key}:{kwargs[key]}")   #odwolanie dow artosci
show_band(PO="Ala", manager= "Kot", Dev="Jezus")
# Ala
# PO:Ala
# manager:Kot
# Dev:Jezus

# ●	*args przechowuje argumenty w postaci zbliżonej do tego, jak to robi krotka
# ●	**kwargs przechowuje argumenty w postaci zbliżonej do tego, jak to robi słownik
print("statystyka")
import statistics as st


def input_data(list):
    aryt_sum = st.mean(list)
    stand_dev = st. stdev(list)

    return aryt_sum, stand_dev

list = [0, 1, 2, 5, 7, 43]

print(input_data(list))
#tuple (9.666666666666666, 16.536827587740845)


imie = input("imie: ")
print(f"Twoje imie to {imie}")

def main():
    imie = input("imie: ")
    print(f"Twoje imie to {imie}")

if __name__ == "__main__":
    main()
#interpreter szuka def funkcji main iją wykonuje...
# __name__ zmienna specjalna a __main__ to jej możliwa wartość
# interpreter, przetwarzając pliki źródłowe, stwarza automatycznie kilka zmiennych
# specjalnych i nadaje im określone wartości.
# Jeśli plik źródłowy jest plikiem głównym (nie jest wczytywany przez inny skrypt),
# to zmienna specjalna __name__ przyjmuje wartość "__main__”).
# Warunek zatem jest prawdziwy (linia 14) i program przechodzi do realizowania swojej funkcjonalności.
#gdyby Nasz program służył jedynie do rozszerzenia funkcjonalności innego programu i Naszym celem nie
# byłoby jego uruchomienie (a wczytanie tylko jego zawartości), to zmienna __name__ przyjęłaby zupełnie
# inną wartość niż __main__  (warunek if __name__ == “__main__” byłby False).




