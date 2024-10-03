# Ćwiczenie z kodowania
#
# Sprawdź ile unikatowych elementów znajduje się w liście A.
# list_a = [1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 7, 5, 43, 4, 6]

from typing import List


list_a = [1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 7, 5, 43, 4, 6]


def unique_elements_counter(user_list: List[int]) -> int:
    """Function that is used to count unique elements on the list"""

    empty_list = []
    for number in user_list:
        if number not in empty_list:
            empty_list.append(number)
    counter = len(empty_list)
    return counter


print(unique_elements_counter(list_a))


list_a = [1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 7, 5, 43, 4, 6]


def second_unique_elements_counter(user_list: List[int]) -> int:
    """Another function that is used to count unique elements on the list"""

    user_set = set(user_list)
    unique_list = list(user_set)
    second_counter = len(unique_list)
    print(f"The total number of unique elements is: {second_counter}")
    return second_counter


second_unique_elements_counter(list_a)


def third_unique_elements_counter(user_list: List[int]) -> int:
    """AND Another function that is used to count unique elements on the list"""

    user_set = set(user_list)
    second_counter = len(user_set)
    print(f"The total number of unique elements is: {second_counter}")
    return second_counter


third_unique_elements_counter(list_a)