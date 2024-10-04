class Vehicle:
    """Class that represents a vehicle with a specific number of wheels and a paintjob code.
    Attributes:
        wheels_num (int): The number of wheels the vehicle has.
        paintjob_code (int): The code representing the vehicle's paint job.
    """

    def __init__(self, wheels_num_: int, paintjob_code_: int) -> None:
        """Initialize a new vehicle with the given number of wheels and paint job code.
        Args:
            wheels_num_ (int): Number of wheels the vehicle has.
            paintjob_code_ (int): Code representing the paint job.
        """
        self.wheels_num = wheels_num_
        self.paintjob_code = paintjob_code_

    def drive(self) -> None:
        """Simulates the vehicle driving."""
        print("Vehicle has been driving on {} wheels".format(self.wheels_num))


def main() -> None:
    """Create a Vehicle instance and make it drive."""

    audi = Vehicle(4, 103)
    audi.drive()


if __name__ == "__main__":
    main()


