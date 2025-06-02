"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

# Constants
MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
MIN_PRICE = 1.00
MAX_PRICE = 100.00
INITIAL_PRICE = 10.00
FILENAME = "price_simulation_output.txt"  # Output filename

price = INITIAL_PRICE
number_of_days = 0  # Variable to count the number of days

# Open the output file for writing
out_file = open(FILENAME, 'w')

# Print the starting price to the file
print(f"Starting price: ${price:,.2f}", file=out_file)

# List to store each day's prices
prices = []

while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1  # Increment the day counter
    price_change = 0

    # Generate a random integer of 1 or 2 to decide price increase or decrease
    if random.randint(1, 2) == 1:
        # Generate a random floating-point number between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # Generate a random floating-point number between -MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    # Update the price
    price *= (1 + price_change)

    # Store the price for the current day in the list
    prices.append(f"On day {number_of_days} price is: ${price:,.2f}")

# Print all prices after the simulation to the file
for daily_price in prices:
    print(daily_price, file=out_file)

# Close the output file
out_file.close()