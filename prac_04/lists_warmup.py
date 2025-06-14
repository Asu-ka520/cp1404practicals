# numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0]
# A:3
# numbers[-1]
# A:2
# numbers[3]
# A:1
# numbers[:-1]
# A:[3, 1, 4, 1, 5, 9]
# numbers[3:4]
# A:[1]
# 5 in numbers
# A:True
# 7 in numbers
# A:False
# "3" in numbers
# A:False
# numbers + [6, 5, 3]

# Original list
numbers = [3, 1, 4, 1, 5, 9, 2]

# Change to "ten"
numbers[0] = "ten"

# Change to 1
numbers[-1] = 1

# Print all elements except the first two
print(numbers[2:])

# Print whether 9 is an element of numbers
print(9 in numbers)