class Cat:
    """Class of the cat object """

    def __init__(self, name: str, color: str) -> None:
        self.name = name
        self.color = color

    def __str__(self) -> str:
        return f"{self.name} cat is {self.color}"


k = Cat("Mruczek", "black")
# print(k.name)
print(k)