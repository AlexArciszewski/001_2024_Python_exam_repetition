#Tworząc tablicę, możesz od razu definiować jej kształt. Utwórz tablicę b korzystając z parametrów przekazywanych do metody array
# lub wywołując odpowiednie metody
# dla już istniejącej tablicy, tak aby zawierała ona elementy parzyste od 0 do 40 o kształcie 4x5
import numpy as np

even_numbers = np.arange(0, 40, 2)
b = even_numbers.reshape(4, 5)
print(b)

#[[ 0  2  4  6  8]
# [10 12 14 16 18]
# [20 22 24 26 28]
# [30 32 34 36 38]]




#tworzy standardową pythonową listę dziesięciu kolejnych potęg dwójki. W oparciu o tą listę utwórz obiekt array c

a_python_list = [2**x for x in range(10)]
print(a_python_list)

c = np.array(a_python_list)
print(c)

#[  1   2   4   8  16  32  64 128 256 512]