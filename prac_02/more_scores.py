"""CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

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
    """Main function to get the number of scores and write results to a file."""
    num_scores = int(input("Enter the number of scores to generate: "))

    # Validate if the input is a positive integer
    if num_scores <= 0:
        print("Please enter a positive integer.")
        return

    results = []
    for _ in range(num_scores):
        # Generate a random score between 0 and 100 inclusive
        random_score = random.uniform(0, 100)
        result = get_score_status(random_score)
        results.append(f"{random_score:.2f} is {result}")

    # Write results to results.txt
    with open("results.txt", "w") as file:
        for line in results:
            file.write(line + "\n")

    print(f"Results written to results.txt for {num_scores} scores.")


if __name__ == "__main__":
    main()