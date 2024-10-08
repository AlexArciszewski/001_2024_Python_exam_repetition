# Klasa abstrakcyjna to taka klasa której instancji nie możemy stworzyć. Służy ona do tego by z
# niej dziedziczyć i implementować te metody które oznaczone zostały jako abstrakcyjne. Przykład takiej klasy:


from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def method1(self):
        pass

    def method2(self):
        return "Helo!"

    def __str__(self):
        return f'Jestem {self.__class__.__name__}'


class ConcreteClass(AbstractClass):
    def method1(self):
        print("Heeelo!")


print(ConcreteClass())

# Jestem ConcreteClass


from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def method1(self):
        pass

    def method2(self):
        return "Helo!"

# print(AbstractClass())
# TypeError: Can't instantiate abstract class AbstractClass with abstract method method1


from abc import ABC, abstractmethod  # Importujemy klasy do pracy z klasami abstrakcyjnymi

class AbstractClass(ABC):  # Klasa abstrakcyjna, której nie można instancjonować
    @abstractmethod
    def method1(self):
        pass  # Abstrakcyjna metoda, którą musimy zaimplementować w klasie dziedziczącej

    def __str__(self):
        return f'Jestem {self.__class__.__name__}'  # Zwraca nazwę klasy obiektu


class ConcreteClass(AbstractClass):  # Klasa, która dziedziczy po AbstractClass
    def method1(self):
        print("Heeelo!")  # Implementacja abstrakcyjnej metody


print(ConcreteClass())  # Wywołanie metody __str__, wynik: 'Jestem ConcreteClass'

