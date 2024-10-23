#Napisz generator x, który zwróci 10 kolejnych wielokrotności liczby 5 - zaczynając od 5, kończąc na 50 (włącznie).
#Następnie napisz pętlę for, która wypisze kolejne wartości zwracane przez generator (i nie spowoduje wypisania StopIteration Error).



def generator():
    for i in range(5, 51, 5):
        yield i

x = generator()
print(next(x))
print(next(x))

try:
    while True:
        print(next(x))
except StopIteration:
    pass


# Do rpzemyślenia ale wyrzuci Stopiteration
# x2 =(n*5 for n in range(5,11))
# print(x2)
#
# for _ in range(10):
#     print(next(x2))