class Animal:
    """Class representing an animal."""
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    @property
    def age(self) -> int :
        """getter gives the value of  """
        return self.__age

    @age.setter  # setter - ustawia nowa wartosc pola prywatnego
    def age(self, age: int) -> None:
        if age > 0:
            self.__age = age
        else:
            print("Age must be greater than 0.")
    @age.deleter  # deleter - usuwa pole
    def age(self) -> None:
       del self.__age

my_dog = Animal("reksio", 5)
my_dog.age = 3  # Ustawia wiek - korzysta z settera
print(my_dog.age)  # Odczytuje wiek - korzysta z gettera
del my_dog.age  # Usuwa pole - korzysta z deletera


""" 

•	property definiuje się najpierw wybierając nazwę, pod jaką ma być dostępny ukrywany atrybut.
•	Następnie tworzy się metodę o wybranej nazwie z poprzedniego punktu i nad jej definicją dopisuje się komendę @property, opakowującą metodę i mówiącą interpreterowi, że mamy do czynienia ze specjalnym atrybutem.
•	Zapis @property nad definicją metody pozwala ustawić getter, czyli metodę która będzie wykonywana za każdym razem, jeśli ktoś będzie chciał odczytać wartość atrybutu.
•	Dopisanie nad metodą @<nazwa_metody_z_property.setter> daje możliwość ustawienia akcji w przypadku chęci zmodyfikowania atrybutu - tutaj mogą się pojawić przeróżne sprawdzenia, czy wartość jest odpowiedniego typu lub czy mieści się w odpowiednio dobranym zakresie.
•	Metoda z dopiskiem @<nazwa_metody_z_property.deleter> jest tą, która zostanie zawołana w przypadku usunięcia atrybutu (np. komendą del obiekt.nazwa_atrybutu).
•	Zapis @property wykorzystuje mechanizm dekoratorów w Pythonie. Więcej o tym w dalszej części kursu.


"""