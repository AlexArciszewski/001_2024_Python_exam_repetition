from typing import List

class Employee:
    """ Representation of Employee object."""

    def __init__(self, name: str, last_name: str, wage:float) -> None:
        """Initialize a new employee with name, last_name and wage."""
        self.name: str = name
        self.last_name: str = last_name
        self.wage: float = wage

    def salary(self, working_hours: int) ->float:
        """method used to calculate salary by using working hours and wage and connects
                 it to Employee name and surname"""
        salary = self.wage * working_hours
        print(f"Salary of {self.name}, {self.last_name} is {salary}")

    @staticmethod
    def work() -> str:
        """static method with no argument that prints string: I am working"""
        print(""" I'm just an average man with an average life I work from nine to five, hey, hell, I pay the price
                All I want is to be left alone in my average home But why do I always feel like I'm in The Twilight
                Zone? """)

    def __str__(self) -> str:
        return (f" (str) My name is {self.name} {self.last_name} and my wage is {self.wage}.")
    #             f"You can see this thx to this awesome __str__ method It replaces the tom object"
    #             f"when you try to print him in main.")

    def __repr__(self) -> str:
        return (f"My name is {self.name} {self.last_name} {self.wage}. Now you can see only this awesome__repr__ method"
                f"because you printed Emoployee obj it's goes above __str__ method if you unmark str method the __str__ method appears you can "
                f"still use repr method by printing ala with repr")



class Programmer(Employee):
    """Class that represents the programmer object inherited after Employee object"""

    def __init__(self, name:str, last_name:str, wage:float, coding_lang:List[str]) -> None:
        super().__init__(name, last_name, wage)
        self.coding_lang:List[str] = coding_lang

    def write_code(self) -> None:
        print(f"I'm coding in {self.coding_lang}")

    def increase_wage(self, percentage_given:float) -> float:
         """Calculate and print the increased wage of the programmer."""
         increased_wage:float = self.wage + self.wage*percentage_given/100
         print(increased_wage)
         return

    @staticmethod
    def coder_spec()->str:
        print("miauuu")

    def __str__(self)-> str:
        return (f"I am prze {self.name} in {self.coding_lang[0]}")



def main() -> None:
    ala: Employee = Employee('Ala', 'Makota', 150.5)
    ala.salary(160)
    ala.work()
    print(ala) #to wywołuje repr lub str normalnie bylby obj <__main__.Employee object at 0x000002585BDAA680> da str metodę lub repr jak nie ma str
    print(repr(ala)) #da metode repr

    print("Other coder")
    kot_ali: Programmer = Programmer("kot", "ali",300.5,['python','sql','dax'])
    kot_ali.write_code()
    kot_ali.increase_wage(100)
    kot_ali.work() #metoda z klasy głw
    kot_ali.coder_spec() #miau

    print(kot_ali) #I am prze kot in python

if __name__ == "__main__":
    main()
