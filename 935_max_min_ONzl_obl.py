# Pytanie 17 - znajdź różnicę między największą a najmniejszą wartością
# na poniższej liście.
# Zadbaj o to aby rozwiązanie było efektywne.

number_list = [4, 5, 7, -3, 2, 8, -10, 15]

# A
print(max(number_list) - min(number_list))     ##O(N) bo tylkor az przegladamy listę 2 razy przeczytamy listę

# B
the_max_min_diff = max(number_list) - min(number_list)
print(the_max_min_diff)
# 25

#C
number_list.sort()
print(number_list[-1] - number_list[0])
# 25

# D
number_list = [4, 5, 7, -3, 2, 8, -10, 15]
sorted_list = sorted(number_list)
print(sorted_list[-1] - sorted_list[0])    #O(N*log_N)
# 25

# E
number_list = [4, 5, 7, -3, 2, 8, -10, 15]

min = number_list[0]
max = number_list[0]
for number in number_list:
    if number < min:
        min = number
    elif number > max:
        max = number
print(max - min)      #O(N) bo tylkor az przegladamy listę
# 25
