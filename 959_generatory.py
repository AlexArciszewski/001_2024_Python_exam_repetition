# Pytanie 33 - do czego w Pythonie służy słowo kluczowe yield ?
# Napisz przykładowy kod wykorzystujący yield.


#yield służy doz wracanai wartości w generatorach
def zwracaj_liczbe():
    for i in range(10):
        yield i

z = zwracaj_liczbe()
print(z)
# <generator object zwracaj_liczbe at 0x0000018E1C658110>
print(next(z))
# 0
print(next(z))
# 1
print(next(z))
# 2

# Petla da stop iteration error
# for n in range(10):
#     print(next(z))



# obsluga stop iteration
z = zwracaj_liczbe()
try:
    while True:
        print(next(z))
except StopIteration:
    print("Generator się wyczerpał")


print("wyrażenie gen")
y = ('a' * n for n in range(5))        # generator expression - wyrażenie generatorowe
                                       # tworzy generator, który będzie zwracał kolejne wielokrotności stringa 'a'
                                       # zakresie od 0 do 4

for i in range(5):                     # wypisanie kolejnych wartości zwróconych przez obiekt genratora y
    print(next(y))