"""
Zad 1.
Na podstawie poznanych poleceń, wskaż dowolne, które mogłyby świadczyć o tym, że Python jest wysokopoziomowym językiem programowania.

np print, raise, break, continue
"""

""" 
Zad 2. 
Czym jest konkatenacja stringów? Która z poniższych operacji jest możliwa?
1 + 1; “str” + 1; “str” + “ “ + “str”
"""

# print(1 + 1)
#
# print("str" + " " + "str")

"""
Zad 3.
Czy poniższe operacje są poprawne i mają sens?

Jaki będzie output na ekranie?
"""
# liczba1 = int(input("Podaj pierwszy składnik sumy "))
# liczba2 = int(input("Podaj drugi składnik sumy "))
#
# wynik = liczba1 + liczba2
# print(f"Wynikiem jest: {wynik} ")


""" 
Zad 4.
Wskaż nieprawidłowo nazwane zmienne:
nazwa_psa = “Reksio”, nazwaKota = “Filemon”, zmienna = “Junior-Dev Factory”, płeć = “mężczyzna”, WartoscLiczbowa = 5, czyZonaty = False,
czy LubiPsy = False

zmienna = “Junior-Dev Factory”, płeć = “mężczyzna”, WartoscLiczbowa = 5,czy LubiPsy = False
"""

""" 
Zad 5.
Jakiego typu są poniższe zmienne: (w celu uproszczenia, zastosowano tę samą nazwę zmiennej)
z = 5, z = -1, z = 0, z = 0.0, z = -1.123, z = “c”, z = ‘c’, z = “programowanie”, z = False, z = True
int    int     int    float        float    str     str       str                  bool      bool
"""
"""
Zad 6.
Wskaż nieprawidłowe odpowiedniki dla operatorów przypisania:
a += 5 -> a = a + 5
a -= 5 -> a = 5 – a X
a *= 5 -> a = 5 * a X
a*= 5 -> a = a * 5 
a /= 5 -> a = 5/a X  a = a / 5
"""

""" 
Zad 7.
Utwórz w programie zmienne przechowujące Twój wzrost oraz wiek. Zapytaj użytkownika o jego wagę i wzrost. Następnie na podstawie tych informacji oblicz wartość BMI i umieść ją w zmiennej o etykiecie bmi. Wyświetl wartość obliczonego BMI.
Wzór na BMI: bmi = waga / wzrost^2 (wzrost ^2 to proces potęgowania)

"""
# usersHeight = 180
# usersAge = 80
#
# height = int(input("Pls input your height: "))
# weight = int(input("Pls input your weight: "))
# weight = usersHeight
# your_BMI = weight / usersHeight**2
# print(f"your BMI: {your_BMI}")


""" 
Jaki będzie wynik operacji i jakiego będzie on typu:
5 / 2; 1 + 1; 1.0 + 1; 2.0 + 2.0; “napis” + 1; “napis” + “napis”; True + True;
5 % 2; 10 % 2; 20 % 30; 100 % 3; 
100 // 3; 5 // 3; 1 // 3
3**3; 2**2; 2**0

"""
# print(5 / 2)
# print(1.0 + 1)
# print("napis" + 1)
# print(True + True)
# print(5 % 2)
# print(10 % 2)
# print(20 % 30)
# print(100 % 3)
# print(100 // 3)
# print(5 // 3)
#

""" 
Zad 9.
Korzystając z funkcji input(), pobierz dowolny napis od użytkownika. Następnie utwórz nowy string z zamienioną pierwszą literą z ostatnią i wyświetl efekt na ekranie, np.
> Użytkownik wprowadził wyraz “Hello world!”
> Program wydrukuje na ekranie nowy napis: “dello worlH!”

"""

text = input("Give me the the text: ")

first_letter_of_text = text[0]
last_letter_of_text = text[-1]
print(first_letter_of_text)
print(last_letter_of_text)
text2 = text
first_letter_of_text = text2[-1]
print(text2[-1])
list = []
for letter in text:
    list.append(letter)
list[0] = last_letter_of_text
list[-1] = first_letter_of_text
text = ''.join(list)
print(text)


def my_word(text):
    text = input("Give me the the text: ")
    first_letter_of_text = text[0]
    last_letter_of_text = text[-1]
    print(first_letter_of_text)
    print(last_letter_of_text)
    list = []
    for letter in text:
        list.append(letter)
    list[0] = last_letter_of_text
    list[-1] = first_letter_of_text
    text = ''.join(list)
    print(text)


def test_my_word():
    assert my_word("kot") == "tok"


""" 
E   OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

"""

""" 
Zad 10.
Mamy w programie zdefiniowane następujące zmienne: 
a = 5
b = 6
Jak wiesz, jest to typ całkowity (int). Spróbuj przekonwertować (konwertowaliśmy już str na typ int, jak to zrobić
 na odwrót?) te wartości na typ str i następnie dokonaj konkatenacji stringów. Efektem powinien być napis: “56”.

"""

a = 5
b = 6

c = str(a)
d = str(b)
print(c + d)

""" 
Zad 11.
Utwórz dwa dowolne stringi o różnych wartościach. Utwórz trzeci napis, który będzie się składał z pierwszej połówki 
pierwszego napisu oraz drugiej połówki drugiego napisu. Skorzystaj z ujemnych indeksów.
imie1 = “Kacper” 
imie2 = “Lucjan”
imie3 = “Kacjan”

"""
imie1 = "Kacper"
imie2 = "Lucjan"
imie3 = "Kacjan"
imie4 = imie1[:3]
imie5 = imie2[-3:]
print(imie4)
print(imie5)
imie6 = imie4 + imie5
print(imie6)

""" 
Zad 12.
Co oznacza zapis tekst1 = tekst2[:]?

"""
tekst1 = "tekst2"[:]  # duplikat
tekst2 = "tekst2"[:1]  # slicing od 1 elementu czyli tylko 1szy wyprintuje
tekst3 = "tekst2"[:2]
print(tekst1)
print(tekst2)
print(tekst3)

"""
Zad 13.
Dlaczego w programowaniu istnieje konieczność korzystania z tzw. kodów ASCII?
odp: Aby zapisac tekst na kod binarny.
"""

""" 
Zad 14.
Znajdź przykłady 3 sposobów na szyfrowanie znaków w systemach informatycznych i zapoznaj się z ich działaniem 
(jakie operacje matematyczne przeprowadzają?). 

szyfrowanie binarne, kod Cezara
"""
