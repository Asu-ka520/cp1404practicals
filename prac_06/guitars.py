"""
CP1404 Practical - Guitars program
"""

from guitar import Guitar


def main():
    """Guitar program, using Guitar class."""
    print("My guitars!")

    # Create a list to store all my guitars
    guitars = []

    # Get user input for guitars - i'll add some test data first
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    # Get user inputs for new guitars
    name = input("Name: ")
    while name != "":  # keep going until empty name
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        # add new guitar to collection
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")

        # get next guitar name
        name = input("\nName: ")

    # sort guitars by yea
    # i'm not sure if this is the best way, but it works
    guitars.sort(key=lambda guitar: guitar.year)

    # Display the collection of guitars
    if guitars:  # check if list is not empty
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"

            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:,.2f}{vintage_string}")
    else:
        print("No guitars in the collection!")


# run the program
if __name__ == '__main__':
    main()