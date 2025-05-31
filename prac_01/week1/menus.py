# get name
# display menu
# get choice
# while choice != Q
#    if choice == H
#        display "hello" name
#    else if choice == G
#        display "goodbye" name
#    else
#        display invalid message
#    display menu
#    get choice
# display finished message

def main():
    # Get username
    name = input("Enter name: ")

    # Display menu and get the first choice
    menu = "(H)Hello(G)Goodbye(Q)Quit"
    print(menu)
    choice = input(">>> ").strip().upper()

    # Loop until the user chooses to quit
    while choice != 'Q':
        if choice == 'H':
            print(f"Hello {name}")
        elif choice == 'G':
            print(f"Goodbye {name}")
        else:
            print("Invalid choice")

        # Display
        print(menu)
        choice = input(">>> ").strip().upper()

    print("Finished.")

# run the program
if __name__ == "__main__":
    main()