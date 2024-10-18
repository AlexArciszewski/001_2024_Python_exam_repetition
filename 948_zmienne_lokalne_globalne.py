# Pytanie 25 - co zostanie wypisane w wyniku wykonania poniższego kodu?

x = 10      #zmienna globalna

def f():
    global x        #odnosimy się do zmienej globalnej 10
    x = 111         #za x przyjmujemy 111
    y = 12          #za y orprzyjmujemy 10
    print(x, y)     # po wywołaniu funkcji 111 12

f()
print(x)            #wydrukuje 111

x = 5       #zmienna globalna poza cialem funkcji


def f():
    x = 11
    #zmienna lokalna w ciele funkcji zmienna wykorzystywana podczas wywołania funkcji
    print(x)

f()        #11
print(x)    #5 bo nie ma global czyli wywołujemy zmienną globalna

