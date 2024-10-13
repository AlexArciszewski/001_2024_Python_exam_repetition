# Wypisz zawartość listy A dodając przed każdym elementem kolejny numer.
# Zacznij numerowanie od 0.


# A = [1, 1, 4, 9]

A = [1, 1, 4, 9]
# lista krotek nie jest to dobre rozwiazanie:[(0, 1), (1, 1), (2, 4), (3, 9)]
print(list(enumerate(A, start=0)))

# Dobre rozwiazanie
for num, number in enumerate(A):
    print(num, number)

# 0 1
# 1 1
# 2 4
# 3 9