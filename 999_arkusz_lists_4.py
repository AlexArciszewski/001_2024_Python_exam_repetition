first_list = [1, 2, 3, 4, 5]
second_list = [7, 8, 9, 10]

# for num in first_list:
#     if num in second_list:
#         print("TAK")
#     else:
#         print("Nie")

first_set = set(first_list)
second_set = set(second_list)

if first_set.intersection(second_set):
    print('Tak')
else:
    print("Nah")


