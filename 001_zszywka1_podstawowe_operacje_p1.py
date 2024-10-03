print('hello World')
imie = 'Ala'
nazwisko = 'Makota'
rok_urodzenia = 2010
srednia_ocen = 4.8

print(imie, nazwisko, rok_urodzenia, srednia_ocen)

print("Hej, {} {} {} {}".format(imie, nazwisko, rok_urodzenia, srednia_ocen))
#Format na binarny:
print("{0:b}".format(0))
print("{0:b}".format(1))
print("{0:b}".format(2))
print("{0:b}".format(3))
print("{0:b}".format(4))

#Operacje
# +	dodawanie	a + b
# -	odejmowanie	a - b
# *	mnożenie	a* b
# /	dzielenie (wynikiem jest liczba zmiennoprzecinkowa float)	a / b, np. 5 / 1 = 5.0
# 5 / 2 = 2.5
# //	Dzielenie całkowite (wynikiem jest zawsze liczba całkowita int, jeżeli wynik wychodzi z częścią dziesiętną, to jest ona dosłownie ,,odcinana”)	a // b, np.
# 5 // 2 = 2
# 9 // 3 = 3
# 10 // 3 = 3
# 14 // 3 = 4
# %	modulo (inaczej sama reszta z dzielenia)	a % b, np.
# 5 % 2 = 1, bo 5 / 2 = 2 r 1
# 10 % 2 = 0, bo 10 / 2 = 5 r 0
# 3 % 10 = 3, bo 3 / 10 = 0 r 3
# ptęgowanie a**b
#2 ** 3 = 8
#3 ** 2 = 9

# Operator	Przykład	Odpowiednik
# =	        a = 5 	        a = 5
# +=	    a += 5	     a = a + 5
# -=	    a -= 5	    a = a - 5
# *=	    a *= 5	    a = a * 5
# /=	    a /= 5	    a = a / 5
# //=	    a // = 5	a = a // 5
# %=	    a %= 5	    a = a % 5
# **=	    a **= 5	    a = a ** 5
#string niemutowalny +można przeiterować wrzucić do listy i wtedy zmeinic 1szy element


napis = "JuniorDevFactory - Twój mentor w programowaniu!"
print(napis[len(napis) - 1])
print(napis[-1])
#print(napis[len(napis)]) to da błąd.
#konkatenacja stringów
wyraz_a = "Kocham"
wyraz_b = "Programować"
wyraz_c = wyraz_a + " " + wyraz_b
print(wyraz_c) # wyświetli “Kocham Programować”

napis = "JuniorDevFactory - Twój mentor w programowaniu!"
print(napis[-2]) # wyświetla 'u'
print(napis[-5:-1]) # wyświetla 'aniu'
print(napis[-5:])
print(napis[:]) # wyświetla skopiowany w całości napis (odpowiednik dla [pierwszy_indeks:końcowy_indeks])
print(napis[-5:])

napisNowy = "Ala ma Koty"
print(napisNowy[len(napisNowy) - 1])
print(napisNowy[:2])
print(napisNowy[10])
print(napisNowy[-11])
print(napisNowy[-11:-8])
print(napisNowy[0:3])
print(napisNowy[:])
print(napisNowy[0:-1])
print(napisNowy[0:-1:2])