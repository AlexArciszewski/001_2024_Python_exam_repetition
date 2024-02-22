# Zad 1.
# Poproś użytkownika o podanie 3 dowolnych długości boków trójkąta. Sprawdź, czy jest to trójkąt prostokątny
# (wykorzystaj własność trójkąta prostokątnego, która mówi że suma kwadratów dwóch dowolnych boków jest równa
# kwadratowi długości trzeciego).

a = int(input("Input the first side of the triangle."))
b = int(input("Input the second side of the triangle."))
c = int(input("Input the third side of the triangle."))

if a**2 + b**2 == c**2:
    print("The triangle is right-angled")
else:
    print("The triangle is not right-angled")

