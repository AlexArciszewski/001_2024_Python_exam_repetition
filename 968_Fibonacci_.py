# Pytanie 40 - ciąg Fibonacciego to ciąg liczb, którego:
# - zerowy element wynosi 0
# - pierwszy element wynosi 1
# - każdy kolejny element jest sumą dwóch poprzedzających go elementów.
# Napisz funkcję, która zwróci n-ty element ciągu Fibonacciego.

# number ; 1, 2, 3, 4, 5, 6, 7, 8,  9
# fibo-el: 0, 1, 1, 2, 3, 5, 8, 13, 21



import pytest


def fibonacci(number) -> int:
    """fibonacci sequence"""
    lenght_list = []
    for number in range(1, number+1):
        lenght_list.append(number)
    # print(lenght_list)
    # print(len(lenght_list))

    fibo_list = []
    fibo_list.append(0)
    fibo_list.append(1)
    num_existed_fibo_list = len(fibo_list)
    # print(fibo_list[0])


    for _ in range(len(lenght_list) - num_existed_fibo_list):    #-2 bo już 2 elementy dodałem
        next_fibo_num = fibo_list[-1] + fibo_list[-2]
        fibo_list.append(next_fibo_num)
    # print(fibo_list)
    print(fibo_list[-1])
    return fibo_list[-1]


fibonacci(9)

print("\n Opcja nr 2 \n")


# @pytest.mark.parametrize("number,expected",[(1, 1), (9, 21)])
# def test_fibonacci(number: int, expected: int) -> None:
#     assert fibonacci(number) == expected

#rekurencja

def fibonacci_r(n):
    if n <= 1:
        return n
    return fibonacci_r(n - 1) + fibonacci_r(n - 2)


print(fibonacci_r(10))

#zlożoność O(2^N)

print("\n Opcja nr 3 \n")


def fibonacci_l(n):     #O(n)
    p, d = 0, 1
    for _ in range(n):
        p, d = d, p+d
    return p


print(fibonacci_l(10))

