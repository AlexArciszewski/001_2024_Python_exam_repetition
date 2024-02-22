# Zad 1.
# Napisz program wydrukowywujący poniższy wzór:
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


for i in range(5):
    print("*" * (i+1))

for i in range(5,0,-1):
    print("*" * (i + -1))