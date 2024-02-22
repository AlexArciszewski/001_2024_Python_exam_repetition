# Zad3.
# Czy poniższe operacje są poprawne i mają sens?
#
# Jaki będzie output na ekranie?

l1 = input("l1 ")
l2 = input("l2 ")
score = l1 + l2
print("score: ", score)

#wynik w psotaci stringów bo nie ma rzutowania

# Zad 4
# Wskaż nieprawidłowo nazwane zmienne:
# nazwa_psa = "Reksio" #ok
# nazwaKota = "Filemon" #ok
# zmienna = "Junior-Dev Factory" #nie
# płeć = "mężczyzna"   #nie znaki pl
# WartoscLiczbowa = 5 #nie z duzej
# czyZonaty = False       #ok
# czy LubiPsy = False     #nie ok

# Zad 5.
# Jakiego typu są poniższe zmienne: (w celu uproszczenia, zastosowano tę samą nazwę zmiennej)
# z = 5, z = -1, z = 0, z = 0.0, z = -1.123, z = “c”, z = ‘c’, z = “programowanie”, z = False, z = True
# int,float,str,bool

# Zad 6.
# Wskaż nieprawidłowe odpowiedniki dla operatorów przypisania:
# a += 5 -> a = a + 5 ok
# a -= 5 -> a = 5 – a   zle
# a *= 5 -> a = 5 * a  zle ale mnożenie jest przemienne
# a*= 5 -> a = a * 5  dobrze
# a /= 5 -> a = 5/a   zle


#Zad 7
# Utwórz w programie zmienne przechowujące Twój wzrost oraz wiek.
# Zapytaj użytkownika o jego wagę i wzrost. Następnie na podstawie tych informacji oblicz
# wartość BMI i umieść ją w zmiennej o etykiecie bmi. Wyświetl wartość obliczonego BMI.
# Wzór na BMI: bmi = waga / wzrost^2 (wzrost ^2 to proces potęgowania)

height = float(input("What's your height [m]? "))
weight = float(input("Whats your weight?  [kg]"))

bmi = weight/height**2
print(f" your bmi is: {bmi}")

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


# Zad 9.
# Korzystając z funkcji input(), pobierz dowolny napis od użytkownika.
# Następnie utwórz nowy string z zamienioną pierwszą literą z ostatnią i wyświetl efekt na ekranie, np.
# >Użytkownik wprowadził wyraz “Hello world!”
# > Program wydrukuje na ekranie nowy napis: “dello worlH!”
#
# Podpowiedź:
# Spróbuj wykonać tę operację, działając jedynie na oryginalnym napisie. Czy jest to możliwe?
#string jest niemutowalny....trzeeba slicing
word = input("Pls give me the word: ")
total = len(word) -1
new_first = word[total]
new_last = word[0]
middle = word[1:-1]
print(f"The modified word is {new_first}{middle}{new_last}")

# Mamy w programie zdefiniowane następujące zmienne:
# a = 5 b = 6
# Jak wiesz, jest to typ całkowity (int). Spróbuj przekonwertować (konwertowaliśmy już str na typ int, jak to zrobić na odwrót?)
# te wartości na typ str i następnie dokonaj konkatenacji stringów. Efektem powinien być napis: “56”.

a = 5
b = 6
c = str(a)
d = str(b)
print(c+d)


# Zad 11.
# Utwórz dwa dowolne stringi o różnych wartościach. Utwórz trzeci napis, który będzie się składał z pierwszej połówki pierwszego
# napisu oraz drugiej połówki drugiego napisu. Skorzystaj z ujemnych indeksów.
# imie1 = “Kacper”
# imie2 = “Lucjan”
# imie3 = “Kacjan”


s1 = "Tomasz"
s2 = "Staszek"
s3 = s1[0:4]+s2[3:]
print(s3)
s4 = s1[:-2]+s2[-4:]
print(s4)

# Zad 12.
# Co oznacza zapis tekst1 = tekst2[:]?

s5 = "deser"
s6 = s5[:]
print(s6)
# tekst1 = tekst2

# Zad 13.
# Dlaczego w programowaniu istnieje konieczność korzystania z tzw. kodów ASCII?

# np. szyfrowanie ciągów znaków?

# Kod ASCII to standardowy system kodowania znaków, który przyporządkowuje liczbom dziesiętnym i/lub heksadecymalnym zestawy
# znaków używanych w językach tekstowych i komunikacji komputerowej. Oto kilka głównych powodów korzystania z kodu ASCII:
#
#Jednoznaczność reprezentacji: Kod ASCII zapewnia jednoznaczną reprezentację znaków, co pozwala na spójne zrozumienie i
#przekazywanie informacji między różnymi systemami komputerowymi.
#
#Komunikacja między systemami: Kod ASCII umożliwia jednolitą reprezentację znaków w różnych systemach operacyjnych i platformach,
# co ułatwia wymianę danych między różnymi programami i urządzeniami.
#
#Programowanie i tekst: W kodowaniu ASCII używane są liczby dziesiętne do reprezentacji znaków, co pozwala na ich łatwe wykorzystywanie
# w programowaniu oraz manipulację tekstową.
#
# Interoperacyjność: Dzięki ujednoliconej reprezentacji znaków, programy napisane w różnych językach programowania lub działające na
# różnych platformach mogą ze sobą współpracować, przekazując dane w postaci tekstowej.
#
#Klawiatury i urządzenia wejścia: Kod ASCII jest używany do przyporządkowania unikalnych numerów (kodów) dla różnych klawiszy na klawiaturze
# komputerowej, co umożliwia ich jednoznaczną identyfikację.
#
#Tekst w komunikacji sieciowej: W wielu protokołach komunikacyjnych, takich jak HTTP czy SMTP, dane tekstowe są przesyłane z wykorzystaniem
# kodu ASCII, co ułatwia zrozumienie i interpretację komunikatów.



