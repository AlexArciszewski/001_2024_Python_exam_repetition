# Działa podobnie do list comprehension, ale zwraca generator
# (czyli obiekt, który generuje wartości na bieżąco zamiast przechowywać je w pamięci).


squares_gen = (x**2 for x in range(10))
print(next(squares_gen))
# 0
print(next(squares_gen))
# 1
print(next(squares_gen))
# 4
print(next(squares_gen))
# 9
print(next(squares_gen))
# 16

# Opcja nr 2 pobierania danych z generatora

for square in squares_gen:
    print(square)
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81