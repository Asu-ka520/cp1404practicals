"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or special characters
so that they can be used with dot notation like this.
"""

from car import Car


def main():
    """Demo test code to show how to use car class."""
    # first lets make a new car with 180 units of fuel
    my_car = Car("My car", 180)
    # then lets drive it 30 kms
    my_car.drive(30)
    # print car info
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)  

    # create a second car with name "Limo" that has 100 units of fuel
    limo = Car("Limo", 100)
    # add 20 more units of fuel to this new car
    limo.add_fuel(20)
    # print out fuel after adding
    print("limo fuel =", limo.fuel)
    # attempt to drive 115 km
    km_driven = limo.drive(115)
    # print out how far we actually drove
    print(f"The limo drove {km_driven} km")
    # print car info again
    print("limo fuel =", limo.fuel)
    print("limo odo =", limo.odometer)
    print(limo)

    # maybe lets try with a sports car
    sports_car = Car("Ferrari", 50)
    sports_car.drive(25)  # drive a bit
    print(f"Ferrari drove {sports_car.odometer} km")
    print(sports_car)  # see what happens when we print


main()