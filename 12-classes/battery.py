from car import Car

class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=123):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f'This car has a {self.battery_size}-kWh battery.')

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()