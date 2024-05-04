# def add_number(a, b, c):
#     return a + b + c

def add_number(a: int, b: int, c: int) -> int:
#int bo funkcja zwraca int sume która jest liczbą
    return a + b + c

print(add_number(1,1,1))
# 3

x = (add_number(1,1,1))
print(x)
# 3


def add_number2(a: int, b: int, c: int) -> None:
#None bo funkcja nie zwraca nic a printuje. jak funkcjaniczego nie printuje w Python to zwraca None
    print( a + b + c)

add_number2(1,2,3)
# 6