

# Zad 8.
# Jaki będzie wynik operacji i jakiego będzie on typu:
# 5 / 2; 1 + 1; 1.0 + 1; 2.0 + 2.0; “napis” + 1; “napis” + “napis”; True + True;
# 5 % 2; 10 % 2; 20 % 30; 100 % 3;
# 100 // 3; 5 // 3; 1 // 3
# 3**3; 2**2; 2**0

a = 5 / 2
print(a)
b = 1.0 + 1
print(b)

# c = "napis" + 1
# print(c)
# Traceback (most recent call last):
#   File "C:\Users\arcis\PycharmProjects\DM_powtorka_P1\003_zszywka1_3_zadanie_03.py", line 61, in <module>
#     c = "napis" + 1
#         ~~~~~~~~^~~
# TypeError: can only concatenate str (not "int") to str


d = 'napis' + 'napis'
print(d)
# napisnapis

e = True + True
print(e)


print(10 % 2)
print(20 % 30)
print(100 % 3)
print(100//3)
print(5//3)
print(1//3)

print(3**3)
print(2**2)
print(2**0)

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
