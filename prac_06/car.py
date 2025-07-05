"""
CP1404/CP5632 Practical - Car class example
"""
class Car:
    """Represent a Car object thingy."""

    def __init__(self, name="", fuel=0):
        """Initialise a Car instance.

        fuel: float, one parameter for fuel in litres
        name: string, name of the car
        """
        self.name = name  # name of car
        self.fuel = fuel  # amount of fuel
        self.odometer = 0  # the car starts with 0 km

    def __str__(self):
        """Return a string representation of a Car object."""
        # this returns a string with car details
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel = self.fuel + amount  # add fuel to car
        # print(f"Added {amount} units of fuel.")

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        # check if we have fuel
        if distance > self.fuel:
            # not enough fuel
            distance_driven = self.fuel  # can only drive as far as fuel allows
            self.fuel = 0
        else:
            # we have enough fuel
            self.fuel = self.fuel - distance
            distance_driven = distance
        self.odometer = self.odometer + distance_driven
        return distance_driven