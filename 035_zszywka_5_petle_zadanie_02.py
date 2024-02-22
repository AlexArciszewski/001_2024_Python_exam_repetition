# Zad. 2
# Napisz program wyświetlający liczby całkowite z przedziału <100; 50> w porządku malejącym.
# Wykonaj to na pętli for i while.

for i in range(100, 49, -1):
    print(i)


max_num = 100
min_num = 50


i = 100
while i >= 50:
    print(i)
    i -= 1
