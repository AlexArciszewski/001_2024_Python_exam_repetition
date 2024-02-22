# Zad 2.
# Napisz program pobierający od użytkownika liczbę n i wyświetlający wartość sumy 1 + 2 + 3 + … + n.
# Podpowiedź:
# Aby obliczyć sumę, należy przeprowadzić instrukcje: suma += wartosc


number = int(input("pls give me the number: "))
box = []
for i in range(number + 1):
    box.append(i)
print(sum(box))