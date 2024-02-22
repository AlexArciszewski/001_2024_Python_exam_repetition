# Zad 3.
# Utwórz listę przechowującą 10 dowolnych liczb podanych przez użytkownika za pomocą input(). W celu pobierania i
# umieszczania danych od usera, zastosuj pętle. Następnie wyświetl z listy tylko liczby parzyste.
number_box = []
for i in range(10):
    number = int(input("pls give me the number: "))
    number_box.append(number)
for num in number_box:
    if num % 2 == 0:
        print(num)
