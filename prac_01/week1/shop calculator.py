def get_price_input(item_number):
    # Get the price of a single item
    price = float(input(f"Price of item {item_number}: "))
    return price

def calculate_total_price():
    # Ask user for the number of items
    num_items = int(input("Number of items: "))

    if num_items < 0:
        print("Invalid number")
        num_items = int(input("Number of items: "))

    total_price = 0.0

    # Loop through each item to get its price
    for i in range(1, num_items + 1):
        price = get_price_input(i)
        total_price += price

    # Check if total price is more than 100
    if total_price > 100:
        discount = total_price * 0.10
        total_price -= discount
        print(f"A discount of $ {discount:.2f} has been applied.")

    # Show the total price
    print(f"Total price for {num_items} items is $ {total_price:.2f}")

# Run the program
calculate_total_price()