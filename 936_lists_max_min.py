# Sprawdź i wypisz (True lub False) czy największy element na liście A jest większy niż liczba 99.


A = [x**2 + 3 for x in range(10)]

# list comprehension boolean
result = [True if number > 99 else False for number in A]
print(result)


result = max(A) > 99
print(result)

print(True if max(A) > 99 else False)