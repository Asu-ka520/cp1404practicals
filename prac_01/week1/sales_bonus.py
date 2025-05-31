"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, bonus is 15%.
"""
# Get initial sales
sales = float(input("Enter sales: $"))

# Loop
while sales >= 0:
    # Calculate bonus
    if sales < 1000:
        bonus = sales * 0.10
    else:
        bonus = sales * 0.15

    # Display
    print(f"Bonus: ${bonus:.2f}")

    sales = float(input("Enter sales: $"))

# Display when sales is negative
print("Exiting program.")