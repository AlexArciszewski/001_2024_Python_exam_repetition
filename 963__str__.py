# Pytanie 36 - wykorzystajmy klasę Pies i obiekt maly_pies z poprzedniego pytania.
# Co stanie się gdy wypiszemy print(maly_pies)?
# Co zrobiłbyś, aby wydrukowana w ten sposób informacja zawierała imie i rase psa?

class Dog:
    def __init__(self, name: str, breed:str) ->None:
        self.name = name
        self.breed = breed

# zdefiniowanie w klasie metody __str__ pozwala sformatować tekst, który zostanie wypisany w wyniku:
# wykonania funkcji print na obiekcie danej klasy - print(obiekt)
# wywołania funkcji str od obiektu klasy  - str(obiekt)
    def __str__(self) -> str:
        return f"Dog breed {self.breed} has a name {self.name}"

middle_dog = Dog("mMatjerk", "wolf")
print(middle_dog)