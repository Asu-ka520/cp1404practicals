import random

"""CP1404/CP5632 - Practical
Broken program to determine score status
"""

def get_score_status(score):
    """Returns the status based on the user's score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    """Main function to get user's score and print the result."""
    user_score = float(input("Enter score: "))
    result = get_score_status(user_score)
    print(result)

    # Generate a random score between 0 and 100
    random_score = random.uniform(0, 100)
    print(f"Random score: {random_score:.2f}")
    random_result = get_score_status(random_score)
    print(random_result)

if __name__ == "__main__":
    main()