# Zad 7.
# Napisz program wyznaczający n (podawane przez użytkownika) pierwszych liczb ciągu Fibonacciego. Przykład:
# dla n = 5
# 0, 1, 1, 2, 3, 5
number_box = []
n = int(input("number: "))
a = 0
b = 1
start = 0

print(start)
print(start + b)
for i in range(1, n):

    c = a + b
    a = b
    b = c
    print(b)

