"""Test file for Guitar class"""

from guitar import Guitar


def run_tests():
    """Tests for Guitar class."""
    print("Testing Guitar class...")

    # first guitar
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    # create a guitar
    guitar = Guitar(name, year, cost)
    # test get_age() - 2024 - 1922 = 102
    guitar_age = guitar.get_age()
    print(f"{name} get_age() - Expected 102. Got {guitar_age}")

    # test is_vintage()
    vintage_status = guitar.is_vintage()
    print(f"{name} is_vintage() - Expected True. Got {vintage_status}")

    # test another guitar
    name2 = "Another Guitar"
    year2 = 2013

    # create second guitar
    guitar2 = Guitar(name2, year2, 1234.56)
    guitar2_age = guitar2.get_age()
    # test get_age() - 2024 - 2013 = 11
    print(f"{name2} get_age() - Expected 11. Got {guitar2_age}")

    # test is_vintage()
    vintage_status2 = guitar2.is_vintage()
    print(f"{name2} is_vintage() - Expected False. Got {vintage_status2}")

if __name__ == '__main__':
    run_tests()