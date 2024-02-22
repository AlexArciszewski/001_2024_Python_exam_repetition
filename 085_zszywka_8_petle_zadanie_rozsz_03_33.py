# Zad 3
# W trakcie Wigilii Bożego Narodzenia, pięciu członków rodziny: Adam, Stanisław, Joanna, Kornelia i Kacper składają sobie
# życzenia. Stwórz program, który wyświetli wszystkie możliwe połączenia między członkami
# rodzin, jakie mogą zajść w trakcie składania sobie życzeń, np.
# Adam - Stanisław, Adam - Joanna, Adam - Kornelia, Adam - Kacper itd.


list_of_names = ["Adam", "Stanisław", "Joanna", "Kornelia", "Kacper"]

for i in range(len(list_of_names)):
    for j in range(i+1, len(list_of_names)):
        print(list_of_names[i], " - ", list_of_names[j])

# This program uses two nested loops to generate all possible combinations of two family members.
# The outer loop iterates over each family member, and the inner loop starts from the next member
# to avoid repetition. The program then prints out the combination of the two family members.
# The output will be: