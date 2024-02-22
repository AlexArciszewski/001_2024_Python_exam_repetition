# Zad 11.
# Wydrukuj za pomocą pętli i symbolu gwiazdki poniższe kształty:
# ●	prostokąt 7 x 6, czyli:
# *******
# *******
# *******
# *******
# *******
# *******

for _ in range(8):
    print("*******")



#
# ●	kwadrat 5 x 5 bez wypełnionego środka (zastosuj instrukcje warunkowe):
#
# *****
# *   *
# *   *
# *   *
# *****

# for i in range(8):
#     if i == 0 and i == 5:
#         print("*******")
#     for i in range(1,3):
#         print("*   *")
# rozmiar kwadratu
size = 5

# wypełnij kwadrat gwiazdkami
for i in range(size):
    for j in range(size):
        # jeśli warunek (tutaj brak wypełnienia środka) jest spełniony
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#
# ●	Choinkę o wysokości 5:
#
#          *
#         ***
#        *****
#       *******
#      *********
#
# Podpowiedź:
# Wykorzystaj pętle zagnieżdżone (pętla umieszczona w innej pętli), gdzie pętla zewnętrzna będzie służyła do
# przechodzenia po wierszach, a pętla wewnętrzna do rysowania gwiazdek w obrębie wiersza.


height = 5
tree = ""

for i in range(height):
    stars = '*' * (2 * i + 1)
    tree += stars.center(2 * height - 1) + "\n"

print(tree)

for i in range(height):
    for j in range(height + i):
        tree += " " if j < height -i - 1 else "*"
    tree += "\n"
