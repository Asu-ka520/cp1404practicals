import os

def main():
    """Main function to check the current directory and get the password."""
    current_directory = os.getcwd()
    print(f"The files and folders in {current_directory} are:")

    items = os.listdir('.')
    for item in items:
        prefix = "(d) " if os.path.isdir(item) else "(f) "
        print(f"{prefix}\t{item}")

    password = get_password()
    print_asterisks(password)

def get_password():
    """Function to get the password input from the user."""
    return input("Enter your password: ")

def print_asterisks(password, symbol='*'):
    """Function to print asterisks for the password length."""
    print(symbol * len(password))

if __name__ == "__main__":
    main()