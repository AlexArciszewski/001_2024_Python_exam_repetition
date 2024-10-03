# W Pythonie nie ma stricte tuple comprehensions, ale można stworzyć generator i przekazać go do funkcji,
# która tworzy krotki.Przykład:
#
#     Stworzenie krotki za pomocą comprehension:


squares_tuple = tuple(x**2 for x in range(5))
print(squares_tuple)
# (0, 1, 4, 9, 16)