# Polimorfizm – karmienie zwierząt
# Stwórz listę z obiektami klas Pies, Kot, Krowa i za pomocą jednej pętli wywołuj daj_glos() na każdym z nich. Przećwicz działanie polimorfizmu.


from typing import List

class Animal:

    def say_something(self) -> None:
        raise NotImplementedError("say something method  must me implemented in inherited classes")

class Dog(Animal):
    def say_something(self) -> None:
        print("Woof Woof")

class Cat(Animal):
    def say_something(self) -> None:
        print("Miau Miau")

# class FishBob(Animal):
#     pass




def main() -> None:
    #animals:list[Animal] = [Dog(), Cat(), FishBob()]
    animals: list[Animal] = [Dog(), Cat()]
    for animal in animals:
        animal.say_something()









if __name__ == "__main__":
    main()