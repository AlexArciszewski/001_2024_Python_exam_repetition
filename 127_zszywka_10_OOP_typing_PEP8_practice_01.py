
class Human:
    """Class that represents a human with attributes like name, surname, sex, and age"""

    def __init__(self, name: str, surname: str, sex: str, age: int) -> None:
        self.name = name
        self.surname = surname
        self.sex = sex
        self.age = age


def main() -> None:
    first_person = Human("Tom", "Kowalsky", "M", 40)
    second_person = Human("Steve", "Jablonsky", "M", 55)

    print(f"First person is: {first_person.name} {first_person.surname}")
    print(f"Second person is: {second_person.name} {second_person.surname}")


if __name__ == '__main__':
    main()


