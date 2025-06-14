"""
CP1404/CP5632 Practical
Data file -> lists program
"""
FILENAME = "subject_data.txt"

def load_data():
    """Read data from the file formatted like: subject, lecturer, number of students."""
    input_file = open(FILENAME)
    data_list = []  # Initialize an empty list to store data
    for line in input_file:
        print(line)  # View each line of content
        line = line.strip()  # Remove newline characters
        parts = line.split(',')  # Split the data into multiple parts
        parts[2] = int(parts[2])  # Convert the third part to an integer
        data_list.append(parts)  # Append the split parts to data_list
        print(parts)  # View the split result
        print("----------")
    input_file.close()
    return data_list  # Return the nested list

def display_subject_details(data):
    """Display subject details in a readable format."""
    for subject in data:
        subject_code = subject[0]
        lecturer = subject[1]
        number_of_students = subject[2]
        print(f"{subject_code} is taught by {lecturer} and has {number_of_students} students")

def main():
    data = load_data()  # Get the nested list
    print(data)  # Print the raw data (optional)
    display_subject_details(data)  # Display detailed information

