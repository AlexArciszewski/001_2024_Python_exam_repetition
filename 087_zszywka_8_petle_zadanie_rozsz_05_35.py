# Zad 5.
# Stwórz następującą strukturę danych (słownik):
# zamowienia = {"Klient_1335" : {"nazwa_potrawy" : "rosół", "ocena" : 5, "rachunek" : 20.0}, "Klient_222" {"nazwa_deseru” : "lody waniliowe", "rachunek" : 5.0 }}
# Następnie wyświetl nazwy wszystkich klientów i dla każdego z nich stwórz podsumowanie zamówienia:
#
# Przykładowy output:
# Klient_1335:
# nazwa_potrawy rosół
# ocena 5
# rachunek 20.0


zamowienia = {
    "Klient_1335" : {"nazwa_potrawy" : "rosół", "ocena" : 5, "rachunek" : 20.0},
    "Klient_222" : {"nazwa_deseru" : "lody waniliowe", "rachunek" : 5.0 }
    }

# print(zamowienia)

for klient in zamowienia:
    print(klient)
    for order in zamowienia[klient]:
        print(order, zamowienia[klient][order])