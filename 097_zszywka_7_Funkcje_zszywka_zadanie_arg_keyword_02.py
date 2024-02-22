# Zad 2.
# Czym się różni argument od parametru funkcji, default arguments od keyword arguments?

# Parametry bowiem deklarujemy zaraz po nazwie funkcji,
# a argumenty to już konkretne wartości, które przekazujemy do funkcji w momencie jej wywołania!








# Argumenty domyślne funkcji umożliwiają nam automatyczne wstawienie za dany argument wartości, jeżeli
# nie zostanie on wysłany podczas wywołania funkcji.

# Argumenty domyślne ustalane są na końcu listy parametrów z wykorzystaniem operatora przypisania (keywordname=value).

print("argumenty domyslne")

def powitaj(powitanie, imie="Jan", wiek=10, narodowsc ="Polska"):
    print(f"{powitanie}, {imie}. Masz {wiek} lat. Jestes narodowosci:{narodowsc}")
# Hi There,Ala, Makota, Ihaaa
# Hi There,Ala, Makota, Ihaaa

powitaj(powitanie="Hej")
powitaj(powitanie="Witaj")

# Hej, Jan. Masz 10 lat. Jestes narodowosci:Polska
# Witaj, Jan. Masz 10 lat. Jestes narodowosci:Polska