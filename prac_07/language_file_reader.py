"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

import csv
from collections import namedtuple

from programming_language import ProgrammingLanguage

def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    # Open the file for reading
    in_file = open('languages.csv', 'r')
    # File format is now: Language,Typing,Reflection,Year,PointerArithmetic
    # Skip the header
    in_file.readline()
    # All other lines are language data
    for line in in_file:
        parts = line.strip().split(',')
        # Reflection and PointerArithmetic are stored as a string (Yes/No) - convert to Boolean
        reflection = parts[2] == "Yes"
        pointer_arithmetic = parts[4] == "Yes"
        # Construct a ProgrammingLanguage object using all elements (year should be int)
        language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
        languages.append(language)
    in_file.close()

    # Loop through and display all languages (using their str method)
    for language in languages:
        print(language)

main()


def using_csv():
    """Language file reader version using the csv module."""
    in_file = open('languages.csv', 'r', newline='')
    in_file.readline()
    reader = csv.reader(in_file)  # use default dialect, Excel
    for row in reader:
        print(row)
    in_file.close()

# using_csv()

def using_namedtuple():
    """Language file reader version using a named tuple."""
    in_file = open('languages.csv', 'r', newline='')
    file_field_names = in_file.readline().strip().split(',')
    print(file_field_names)
    # Now fields: name, typing, reflection, year, pointer_arithmetic
    Language = namedtuple('Language', 'name typing reflection year pointer_arithmetic')
    reader = csv.reader(in_file)  # use default dialect, Excel

    for row in reader:
        # Convert reflection and pointer_arithmetic to Boolean for demonstration
        row[2] = row[2] == "Yes"
        row[3] = int(row[3])  # year as integer
        row[4] = row[4] == "Yes"
        language = Language._make(row)
        print(repr(language))
    in_file.close()

# using_namedtuple()


def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    Language = namedtuple('Language', 'name typing reflection year pointer_arithmetic')
    in_file = open("languages.csv", "r")
    in_file.readline()
    reader = csv.reader(in_file)
    for row in reader:
        # Convert the relevant fields as above
        row[2] = row[2] == "Yes"
        row[3] = int(row[3])
        row[4] = row[4] == "Yes"
        language = Language._make(row)
        print(f"{language.name} was released in {language.year}")
        print(repr(language))
    in_file.close()

# using_csv_namedtuple()