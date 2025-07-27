"""Taxi class test code."""
from taxi import Taxi

def main():
    """Test the Taxi class."""
    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print(taxi)  # Expected: Prius 1, fuel=60, odometer=40, $0.00
    print("Fare for 40 km:", taxi.get_fare())

    taxi.start_fare()
    taxi.drive(100)
    print(taxi)  # Expected: Prius 1, fuel=0, odometer=100, $0.00
    print("Fare for 100 km:", taxi.get_fare())

if __name__ == '__main__':
    main()