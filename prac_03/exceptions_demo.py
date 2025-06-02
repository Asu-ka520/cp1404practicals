"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Q1:When will a ValueError occur?
# A: when the user inputs a value that cannot be converted to an integer by the int() function.
#
# Q2:When will a ZeroDivisionError occur?
# A: when the user provides a denominator value of zero
#
# Q3:Could you change the code to avoid the possibility of a ZeroDivisionError?
# A:if the denominator is zero before performing the division
# Changes:

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Check if denominator is zero
    if denominator == 0:
        raise ZeroDivisionError  # Manually raise an exception to be caught below

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")




