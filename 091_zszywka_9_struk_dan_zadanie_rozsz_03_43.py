# Zad 3.
# Mając poniższy słownik:
# {‘a’ : 3, ‘b’ : 1, ‘c’ : 10, ‘d’ : 15, ‘e’ : 20}
# dokonaj jego odwrócenia, tzn. niech wartości staną się kluczami, a klucze wartościami.
# Dla powyższego przykładu poprawnym wynikiem będzie:
# {3 : ‘a’, 1 : ‘b’, 10 : ‘c’, 15 : ‘d’, 20 : ‘e’}
some_dict = {
             'a' : 3,
             'b' : 1,
             'c' : 10,
             'd' : 15,
             'e' : 20
            }
#newdict has keys that were values in some_dicts and values that were keys in some_dict
new_dict_keys_list = []
new_dict_values_list = []
print("old dict is", some_dict)

print("working on new dict")
for key in some_dict:
    new_dict_values_list.append(key)

print(f"The values for new dict are:{new_dict_values_list}")

for key in some_dict:
    number = (some_dict[key])
    new_dict_keys_list.append(number)

print(f"The keys for new_dict are: {new_dict_keys_list}")

#
# final_dict = {}
# for key in new_dict_keys_list:
#     for value in new_dict_values_list:
#         final_dict[key] = value
#
# print(final_dict)

# dict from lists
zip_dict = dict(zip(new_dict_keys_list, new_dict_values_list))
print(zip_dict)








print("repetition")

print(some_dict)
# {'a': 3, 'b': 1, 'c': 10, 'd': 15, 'e': 20}
for key in some_dict:
    print(key)
# a
# b
# c
# d
# e
for key in some_dict:
    print(some_dict[key])
# 3
# 1
# 10
# 15
# 20
for items in some_dict.items():
    print(items)
# ('a', 3)
# ('b', 1)
# ('c', 10)
# ('d', 15)
# ('e', 20)

for key in some_dict.keys():
    print(key)
# a
# b
# c
# d
# e
for value in some_dict.values():
    print(value)
# 3
# 1
# 10
# 15
# 20