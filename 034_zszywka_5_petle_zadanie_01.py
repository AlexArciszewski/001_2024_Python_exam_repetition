# Zad. 1
# Napisz program wyświetlający liczby całkowite z przedziału <0; y>,
# gdzie y podaje użytkownik. Wykonaj to na pętli for i while.

user_number = int(input("Give number: "))
for number in range(0, user_number + 1):
    print(number)

user_number = int(input("Give number: "))
while number < user_number + 1:
    print(number)
    number += 1