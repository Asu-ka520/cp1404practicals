"""
CP1404 Practical - Guitar class
"""

CURRENT_YEAR = 2024  # this is the current year for age calculations
VINTAGE_AGE = 50  # guitars 50 or more years old are vintage


class Guitar:
    """Guitar class for storing details about guitars."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        # format the cost to 2 decimal places with comma separators
        guitar_string = f"{self.name} ({self.year}) : ${self.cost:,.2f}"
        return guitar_string

    def get_age(self):
        """Get the age of a guitar based on CURRENT_YEAR."""
        # calculate how old the guitar is
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Determine if a guitar is considered vintage or not based on age."""
        # a guitar is vintage if its age is >= 50
        guitar_age = self.get_age()

        # check if it's vintage
        if guitar_age >= VINTAGE_AGE:
            return True
        else:
            return False
