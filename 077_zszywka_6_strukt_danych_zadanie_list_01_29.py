# Zad 2.
# W pewnej grze liczbowej wylosowano następujące liczby:
# wynik = [12,1,45,76,50,23]. Okazało się jednak, że wylosowane wartości powinny zawierać się w
# przedziale od 1 do 49. Napisz program zastępujący dowolne liczby – nie tylko te konkretne z zadania -
# występujące w liście, które nie spełniają tego kryterium, na wylosowane liczby, które będą je spełniać.
# Program powinien
# także zakomunikować, że znalazł błędną wartość i dokonał dla niej zmiany.
#
# Podpowiedź:
# Użyj modułu random, który trzeba importować, czyli: import random na początku programu. Zawiera on szereg
# funkcji losowych - poczytaj w Internecie o funkcjach losowych w Pythonie 3. Jeśli chcesz wylosować liczbę
# całkowitą z przedziału [a,b], to możesz użyć funkcji losowej: randint(a,b), np. randint(5,10).

import random
from random import sample

base_score = [12, 1, 45, 76, 50, 23]
#numbers higher than 49 must be repaced with other numbers
wrong_numbers = []
good_numbers = []
for number in base_score:
    if number > 49:
        print(f"The wrong number is {number} on {base_score.index(number)}")
        wrong_numbers.append(number)

print(len(wrong_numbers))
print(base_score)

#wrong numbers [76,50]
base_score_cut = base_score
for wrong_number in wrong_numbers:
    base_score_cut.remove(wrong_number)
print(f"Cut list{base_score_cut}")
# list with good numbers[12, 1, 45, 23]

new_numbers =[]
for replace_number in range(1, 50):
    if replace_number not in base_score:
        new_numbers.append(replace_number)
print(new_numbers)
new_chosen_numbers = sample(new_numbers, len(wrong_numbers))
print(new_chosen_numbers)
final_list = []
final_list = base_score_cut + new_chosen_numbers
print(f"The answer is: {final_list}")






# for i in range(len(wrong_numbers)):
    # if len(good_numbers) < len(wrong_numbers):
#         x = random.randint(1,49)
#         good_numbers.append(x)
#
# print(f"{good_numbers} The good numbers")
# [36, 6] The good numbers
#
# for number in good_numbers:
#      for j in range(len(good_numbers)):
#         if number == x:
#           y = random.randint(1,49)
#           good_numbers.insert(good_numbers.index(number), y)
# # #Od tego momentu coś mis ię zapętliło i sie nie wyświetla kod nizej
# print("The result")
# print(good_numbers)
# print(base_score_cut)
# #replacing doubled numbers
# final_score =[]
# base_score_cut.extend(good_numbers)
#
# print(base_score_cut)
#
#

