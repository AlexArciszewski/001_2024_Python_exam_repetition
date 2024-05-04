#typing dla listy

# [[1, 2, 3]]
# list[list[int]]

x: list[list[int]] = []
# działa....

from typing import List

y: List[List[int]] = [[1, 2], [3, 4]]
# mypy C:\Users\arcis\PycharmProjects\001_2024_Python_exam_repetition\9999_typing_03_listy_przekaz_arg_powtorka.py

# Success: no issues found in 1 source file

z: dict[str, str] = {"a": "b"}
# mypy daje blad...error: Incompatible types in assignment (expression has type "Set[str]", variable has type "Dict[str, str]")  [assignment]


from typing import Dict

zz: Dict[str, str] = {"a": "b"}

from typing import Set

set: Set[str] = {"a","b"}


# mypy C:\Users\arcis\PycharmProjects\001_2024_Python_exam_repetition\9999_typing_03_listy_przekaz_arg_powtorka.py
# Success: no issues found in 1 source file


Vector = List[float]


Vectors = List[Vector]

#tworzenie customowych zmiennych i funkcji
def foo1(v: Vectors) -> Vectors:
    pass

# foo1(v)


#Poprawny zapis ale słaby

def foo(output: bool=False):
    pass

# foo()


#dobry zapis...

from typing import Optional

def optionfoo(output: Optional[bool]=False):
    pass

# optionfoo()



from typing import Any

def anyfoo(output: Any):
    pass

# anyfoo("a")



from typing import Sequence


def seqfoo(seq: Sequence[str]):
    pass

seqfoo(("a", "b", "c"))
seqfoo(["a", "b", "c"])
# seqfoo(1) error w mypy
#  error: Argument 1 to "seqfoo" has incompatible type "int"; expected "Sequence[str]"  [arg-type]
#nie jest ważne czy tupa czy lista ważne ze sekwencja elementów będacych stringami

from typing import Tuple
k: Tuple = (1, 2, 3, "hello")
zzz: Tuple[int, int, int] = (1, 2, 3)

# mypy C:\Users\arcis\PycharmProjects\001_2024_Python_exam_repetition\9999_typing_03_listy_przekaz_arg_powtorka.py
# Success: no issues found in 1 source file

from typing import Callable

def callfoo(func: Callable[[int,int],int]) -> None:
    func(1, 2)

#ok

def add(x: int, y: int) -> int:
    return x + y

#ok
