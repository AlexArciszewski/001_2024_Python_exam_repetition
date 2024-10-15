# Pytanie 20 - co otrzymamy w wyniku wydrukowania zawartości poniższych zmiennych?

L = [1, 2, 3, 4, 5, 6]

L1 = [x for x in range(5)]                                  #[1,2,3,4]
L2 = [x**2 for x in L]                                      #[1,4,9,16,25,36]
L3 = [x for x in L if x % 2 == 0]                           #[2,4,6]
L4 = ['Parzysta' if x%2 == 0 else 'Nieparzysta' for x in range(5)]  #['parzysta, ''Nieparzysta','Parzysta','Nieparzysta','Parzysta'] petla idzie od 0 a nie elementow z listy
L5 = [(x, x+10) for x in L]                                 #[(1, 11), (2, 12), (3, 13), (4, 14), (5, 15), (6, 16)]
D1 = {x:x % 2 == 0 for x in L}                              ## wpisz do słownika D1 pary klucz:wartość, gdzie kluczem są elementy z listy L
                                                            # a wartościami True lub False, w zależności od tego czy dany klucz jest podzielny przez 2
#                                                             {1: False, 2: True, 3: False, 4: True, 5: False, 6: True}
print(L1)
print(L2)
print(L3)
print(L4)
print(L5)
print(D1)


for i in range(5):
    print(i)