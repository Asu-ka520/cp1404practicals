def main():
    # Part 1: Number Statistics
    numbers = []  # Initialize an empty list to store the numbers

    # Prompt the user for 5 numbers
    for i in range(5):
        num = float(input(f"Enter number {i + 1}: "))  # Accept user input and convert to float
        numbers.append(num)  # Add the number to the list

    # Output each number
    for number in numbers:
        print(f"Number: {number}")

    # Calculate required statistics
    first_number = numbers[0]
    last_number = numbers[-1]
    smallest_number = min(numbers)
    largest_number = max(numbers)
    average = sum(numbers) / len(numbers)

    # Output the statistics
    print(f"The first number is {first_number}")
    print(f"The last number is {last_number}")
    print(f"The smallest number is {smallest_number}")
    print(f"The largest number is {largest_number}")
    print(f"The average of the numbers is {average:.2f}")

    # Part 2: User Authentication
    usernames = [
        'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
        'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
        'Command', 'ExecState', 'InteractiveConsole',
        'InterpreterInterface', 'StartServer', 'bob'
    ]

    # Ask the user for their username
    input_username = input("Please enter your username: ")

    # Check if the username is in the list of authorized users
    if input_username in usernames:
        print("Access granted")
    else:
        print("Access denied")


# Run the program
main()