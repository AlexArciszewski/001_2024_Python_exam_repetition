# Zad 6.
# Napisz funkcję, która jako argument przyjmuje 10-cio elementową listę liczb całkowitych. Ma ona zwrócić przefilitrowaną
# listę elementów składającą się tylko z liczb dwucyfrowych wyselekecjonowanych z odebranej listy.


import random

ten_el_list = []
for i in range(10):
    ten_el_list.append(random.randint(0,100))
print(ten_el_list)


def two_digit_number_selector(list):
    filtered_list = []
    for number in list:
        if number > 9:
            filtered_list.append(number)

    return filtered_list



print(two_digit_number_selector(ten_el_list))