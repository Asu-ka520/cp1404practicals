from unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar."""
    car = UnreliableCar("Unreliable", 100, 50)
    for i in range(10):
        distance = car.drive(40)
        print(f"Attempt {i + 1}: tried to drive 40km, actually drove {distance}km. Remaining fuel: {car.fuel}")


if __name__ == '__main__':
    main()