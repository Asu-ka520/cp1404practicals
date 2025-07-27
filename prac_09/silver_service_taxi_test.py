from silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print("Fare:", taxi.get_fare())

if __name__ == '__main__':
    main()