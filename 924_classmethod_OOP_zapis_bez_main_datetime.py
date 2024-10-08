from datetime import date


class Worker:
    """Class that holds information about a worker object."""
    def __init__(self, name: str, start_year: int) -> None:
        """constructor"""
        self.name = name
        self.start_year = start_year

    @classmethod  # zamiast staticmethod bo staticmethod nie przyjmuje cls jako pierwszego argumentu
    def from_seniority(cls, name: str, years: int) -> 'Worker':
        """Creates a Worker instance based on years of seniority."""
        return cls(name, date.today().year - years)

    def display(self) -> None:
        """Displays worker's information."""
        print(f"Worker's name:{self.name} \n Worker's start_year:{self.start_year}\n")


w1 = Worker("John", 2000)
w2 = Worker.from_seniority("Elizabeth", 5)

w1.display()
w2.display()