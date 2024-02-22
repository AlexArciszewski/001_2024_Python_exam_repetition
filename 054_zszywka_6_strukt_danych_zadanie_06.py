# Zad 6.
# Wprowadź listę a = [3, 1, 5, 7, 9, 2, 6], wykonaj poniższe polecenia
# i zinterpretuj ich wyniki:
# a) a[3]  7
a = [3, 1, 5, 7, 9, 2, 6]
print(a[3])

# b) a[1:4]
print(a[1:4])
# [1,5,7]

# c) a[3:]
print(a[3:])
# [7, 9, 2, 6]

# d) a[-3:]
print(a[-3:])
# [9, 2, 6]

# e) a[:3]
print(a[:3])
# [3, 1, 5]

# f) a[3:-1]
print(a[3:-1])
a = [3, 1, 5, 7, 9, 2, 6]
# [7, 9, 2]

# g) a[::2]
print(a[::2])
# [3, 5, 9, 6]

# h) a[5:2:-1]
print(a[5:2:-1])
# [2, 9, 7]

# i) sum(a)
print(sum(a))
# 33

# j) 8 in a
print(8 in a)
# False

# k) 4 not in a
print(4 not in a)
# True