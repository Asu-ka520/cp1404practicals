import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


def generate_quick_picks(num_picks):
    quick_picks = []

    # Generate the specified number of picks
    for _ in range(num_picks):
        # Generate unique random numbers for each quick pick
        pick = set()  # Using a set to avoid duplicates
        while len(pick) < NUMBERS_PER_PICK:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            pick.add(number)  # Add the number to the set

        # Sort the pick and convert to list
        sorted_pick = sorted(pick)
        quick_picks.append(sorted_pick)

    return quick_picks


def print_quick_picks(quick_picks):
    for pick in quick_picks:
        # Format each number with leading spaces for alignment
        print(" ".join(f"{num:2}" for num in pick))


def main():
    # Ask the user for the number of quick picks they wish to generate
    num_picks = int(input("How many quick picks? "))

    # Generate the quick picks
    quick_picks = generate_quick_picks(num_picks)

    # Print the formatted quick picks
    print_quick_picks(quick_picks)


# Run the program
main()