# Pytanie 21: co wydrukuje się w wyniku wykonania poniższego kodu?

print(1 == True) # == to operator porównania wartości       True to odpowiednik 1 a False 0
print(1 is True) # is to operator porównania identyczności/tożsamości False 1 to int a true to boolean

print(id(1), id(1), id(True))  # wydrukuj id integera 1 i booleana True  liczba liczba inna liczba

print(2 ** 3 == 10 - 2)        # wydrukuj wynik porównania wartości dwóch równań                True

A = [1,2,3]                    # stworzenie dwóch list o identycznej zawartości
B = [1,2,3]                    # i przypisanych do innych zmiennych A i B
print(A == B)                  # porównanie wartości list A i B                                 True
print(A is B)                  # porównanie identyczności/tożsamośli list A i B                 False

a = 'kotek'                    # stworzenie dwóch stringów o identycznej zawartości
b = 'kotek'                    # i przypisanych do innych zmiennych a i b
print(a == b)                  # porównanie wartości stringów a i b                             True
print(a is b)                  #sprawdzenie że stringi są identyczne. tak bo str sa niemutowalne True listy dadzą Fals
