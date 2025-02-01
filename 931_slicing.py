# Pytanie 15 - napisz funkcję, która sprawdzi czy podany string
# zaczyna się słowem "python" i kończy rozszerzeniem "414_pandas_zmiana_typu_danych_kol_astype_to_numeric.py"
# Przetestuj nią stringi:
# a = "python_moj_kod.py"
# b = "python_notatki.txt"

import pytest

a = "python_moj_kod.py"
b = "python_notatki.txt"


def python_py_checker_func(some_string: str) -> bool:
    """Function that checks whether a string starts with python and ends with 414_pandas_zmiana_typu_danych_kol_astype_to_numeric.py"""
    if some_string.startswith("python") and some_string.endswith("414_pandas_zmiana_typu_danych_kol_astype_to_numeric.py"):
        return True
    else:
        return False


print(python_py_checker_func(a))
print(python_py_checker_func(b))


# def test_python_py_checker_func() -> None:
#     """Testh of function that checks whether a string starts with python and ends with 414_pandas_zmiana_typu_danych_kol_astype_to_numeric.py"""
#     assert python_py_checker_func("python_moj_kod.py") == True
#     assert python_py_checker_func("python_notatki.txt") == False


# Opcja nr 2

def other_python_py_checker_func(some_other_string: str) -> bool:
    if some_other_string[0:6] == "python" and some_other_string[-3:] == "414_pandas_zmiana_typu_danych_kol_astype_to_numeric.py":
        return True
    else:
        return False


print(other_python_py_checker_func("python_moj_kod.py"))
print(other_python_py_checker_func("python_notatki.txt"))


@pytest.mark.parametrize('some_other_string, expected', [("python_moj_kod.py", True), ("python_notatki.txt", False)])
def test_other_python_py_checker_func(some_other_string: str, expected: bool) -> None:
    """Testh of function that checks whether a string starts with python and ends with 414_pandas_zmiana_typu_danych_kol_astype_to_numeric.py"""
    assert other_python_py_checker_func(some_other_string) ==  expected
