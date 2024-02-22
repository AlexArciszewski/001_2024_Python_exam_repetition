print("odliczanie")
for number in range(10, 0, -1):
    print(f"{number} seconds to go.")
print("BOOM")


line = int(input("input the length: "))
for i in range(line):
    for j in range(line):
        print("*", end="")

    print()
# Jeżeli chcemy, aby po wydrukowaniu danego napisu, nie przechodzić do nowej linii
# (domyślne zachowanie printa), ale wstawić spację, to należy przy wyświetlaniu
# danego tekstu, dodać parametr end= ‘ ‘,Jeżeli chcemy, aby po wydrukowaniu danego napisu,
# nie przechodzić do nowej linii (domyślne zachowanie printa), ale wstawić spację,
# to należy przy wyświetlaniu danego tekstu, dodać parametr end= ‘ ‘,


print("*" * 10)
print("inna opcja")

for i in range(5):
    print("*" * 10)

