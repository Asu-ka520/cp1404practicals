"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def print_income_report(incomes):
    """This function will print the income report."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, len(incomes) + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))  # Changed months to num_months

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))  # Using f-string
        incomes.append(income)

    print_income_report(incomes)  # Call the new function to print the report

# Run the program
main()