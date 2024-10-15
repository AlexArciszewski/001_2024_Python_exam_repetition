# Pytanie 19 - wyjasnij jak działa poniższa funkcja.
# Wyjaśnij skąd wzięły się wyniki zwrócone przez poszczególne wywołania funkcji.

def dodaj_do_listy(n, lista=[]):
    lista.append(n)
    print(lista)
#  lista=[] to parametr domyślny czyli jak nie ma podaych dwóch parametrów to przyjmowana za pierwszy parametr jest liczba n w wyołanej funkcji a za drugi przyjmuje sie pustą listę.
# jak sąd wa parametry to wyświetlana jest wywołana lista bo printujemyy w funkcji listę a nie n


dodaj_do_listy(1)      #[1]
dodaj_do_listy(2,[4,5])     #[4,5,2]
dodaj_do_listy(3)       #[1,3] ta lista tworzy się tylko raz a nie jest nowa bo toargument domyślny i uległ zmianie w lsicie domyslnej znajduje sie już 1



def print_name(name = "Ala"):
    print(name)

print_name("Kot")   #Kot
print_name()    #Ala

# Co zostanie wypisane w wyniku wykonania poniższego kodu?

def usun_ostatni_element_listy(lista=[1, 1, 1, 1]):
    lista.pop()
    print(lista)


usun_ostatni_element_listy()        #[1, 1, 1]
usun_ostatni_element_listy([5, 5, 5])   #[5,5]
usun_ostatni_element_listy()       # [1,1]