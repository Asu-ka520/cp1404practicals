from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

def main():
    """Taxi Simulator program."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0

    menu = "q)uit, c)hoose taxi, d)rive"
    print("Let's drive!")
    print(menu)
    choice = input(">>> ").lower()

    while choice != 'q':
        if choice == 'c':
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxis[i]}")
            taxi_choice = int(input("Choose taxi: "))
            if 0 <= taxi_choice < len(taxis):
                current_taxi = taxis[taxi_choice]
            else:
                print("Invalid taxi choice")
        elif choice == 'd':
            if current_taxi:
                current_taxi.start_fare()
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(menu)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxis[i]}")

if __name__ == '__main__':
    main()