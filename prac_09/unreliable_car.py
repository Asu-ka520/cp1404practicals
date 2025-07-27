from car import Car
import random

class UnreliableCar(Car):
    """An unreliable car that may not always drive."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if a random number is less than reliability."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            # Car fails to drive
            return 0