# Zad 1.
# Zdefinuj funkcję, która znajdzie i zwróci indeks największego elementu z przekazanej jako parametr listy
#
# nums = [4, 6, 8, 24, 12, 2]
#
# Dodatkowo:
# Zapoznaj się funkcją enumerate
# z dokumentacji https://book.pythontips.com/en/latest/enumerate.html.
# Spróbuj ją zastosować w rozwiązaniu powyższego zadania.


print("bez enumerate")
nums = [4, 6, 8, 24, 12, 2]


def max_element(num_list):
    max_index = num_list.index(max(num_list))
    return max_index


print(max_element(nums))


print("z enumerate")



nums = [4, 6, 8, 24, 12, 2]


def max_element_with_enum(list_of_numbers):
    """method used to return the position of max element in the list"""
    for counter, value in enumerate(list_of_numbers):
        if value == max(list_of_numbers):
            # print(counter)
            return counter


print(max_element_with_enum(nums))


my_list = ['apple', 'banana', 'grapes', 'pear']
for counter, value in enumerate(my_list):
    print(counter, value)

# Output:
# 0 apple
# 1 banana
# 2 grapes
# 3 pear


my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 100):
    print(c, value)

# Output:
# 100 apple
# 101 banana
# 102 grapes
# 103 pear

my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list)
# Output: [(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]