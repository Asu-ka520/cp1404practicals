# Task 1: Ask the user for their name and write it to name.txt
def write_name_to_file():
    name = input("Please enter your name: ")
    with open('name.txt', 'w') as file:  # Open the file using a context manager
        file.write(name)  # Write the name to the file

# Task 2: Read the name from name.txt and greet the user
def greet_user():
    with open('name.txt', 'r') as file:  # Use a context manager to open the file
        name = file.readline().strip()  # Read and strip any extra whitespace from the name
        print(f"Hi {name}! Welcome!")  # Greet the user with their name

# Task 3: Read the first two numbers from numbers.txt and add them
def add_first_two_numbers():
    with open('numbers.txt', 'r') as file:  # Open numbers.txt with context manager
        numbers = file.readlines()  # Read all lines into a list
        if len(numbers) < 2:  # Ensure there are at least two numbers to read
            print("Not enough numbers provided!")
            return
        first_number = int(numbers[0].strip())  # Convert first number to an integer
        second_number = int(numbers[1].strip())  # Convert second number to an integer
        total = first_number + second_number  # Add the two numbers
        print(f"The sum of the first two numbers is: {total}")  # Print the result

# Task 4: Print the total for all numbers in numbers.txt
def sum_all_numbers():
    total_sum = 0
    with open('numbers.txt', 'r') as file:  # Open numbers.txt with context manager
        for line in file:  # Iterate over each line in the file
            total_sum += int(line.strip())  # Add each number to total_sum
    print(f"The total sum of all numbers is: {total_sum}")  # Print the total sum

# Main code to execute the tasks
if __name__ == "__main__":
    # Task 1: Write name to file
    write_name_to_file()

    # Task 2: Greet the user
    greet_user()

    # Task 3: Create numbers.txt with sample numbers
    with open('numbers.txt', 'w') as file:  # Create numbers.txt and write sample numbers
        file.write("17\n")
        file.write("42\n")
        file.write("400\n")

    # Task 4: Add first two numbers
    add_first_two_numbers()

    # Task 5: Sum all numbers
    sum_all_numbers()