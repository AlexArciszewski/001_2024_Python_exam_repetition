# Co zostanie wydrukowane w wyniku wykonania poniższego kodu?


g = 'jestem globalna'


def f():
    global g
    g = 'teraz jestem lokalna'
    print(g)


f()
print(g)
#w funkcji za globalg wchodzi 'jestem globalna'
#'jestem globalna' zmienia się w 'teraz jestem lokalna'
#funkcja printuje 'teraz jestem lokalna'
# 'teraz jestem lokalna' zmieniła zmienna globalną 'jestem globalna' w funkcji więc
#print(g) drukuje 'teraz jestem lokalna'