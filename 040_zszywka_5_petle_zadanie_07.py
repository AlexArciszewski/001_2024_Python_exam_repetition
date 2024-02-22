# Zad. 7
# Narysuj poniższe kształty:
#
# a)	szlaczek o długości 10

print("*" * 10)
# **********
#
# b)	trójkąt prostokątny o wysokości 4
for i in range(5):
    print("*" * i)
# *
# **
# ***
# ****
#       c) kwadrat o wymiarach 3 x 3
# ***
# ***
# ***

for i in range(3):
    print("*" * 3)

#    d) choinkę o wysokości 5*;
#       *
#      ***
#     *****
#   ** ** ** *
# ** ** ** ** *
#
# Podpowiedź: wykorzystaj
# metodę
# center()
# https: // www.w3schools.com / python / ref_string_center.asp


# Python program to illustrate center()
txt1 = 'Programming'
new_str = txt1.center(20, '*')
print('Centered String:', new_str)

txt2 = 'Welcome'
new_str = txt2.center(15, '!')
print('Centered String:', new_str)

txt3 = 'James'
new_str = txt3.center(10, '@')
print('Centered String:', new_str)


print("choinka")

wysokosc = 5

for i in range(1, wysokosc + 1):
    gwiazdki = '*' * (2 * i - 1)
    if i == 1 or i == wysokosc:
        poziom = (wysokosc * 2 - 1) * ' ' + gwiazdki
    elif i == wysokosc // 2 + 1:
        poziom = (wysokosc * 2 - 3) // 2 * ' ' + gwiazdki + ' ' * (wysokosc - 2) + '*'
    else:
        poziom = (wysokosc * 2 - 3) // 2 * ' ' + gwiazdki + ' ' * (wysokosc - i - i + 2) + '*'
    print(poziom.center(wysokosc * 2 - 1))