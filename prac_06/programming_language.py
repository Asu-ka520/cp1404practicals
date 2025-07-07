"""
CP1404 - ProgrammingLanguage class
"""

class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name_of_lang, typing_style, has_reflection, first_year):
        """Constructor that takes 4 parameters."""
        self.name = name_of_lang
        self.typing = typing_style
        self.reflection = has_reflection  # true or false
        self.year = first_year
        # self.popularity = 0

    def is_dynamic(self):
        """Check if the language is dynamically typed, i think this works."""
        if self.typing == "Dynamic":
            return True
        else:
            return False
        # could just do: return self.typing == "Dynamic"

    def __str__(self):
        """this returns a string representation of a programming language."""
        language_str = f"{self.name}, {self.typing} Typing, "
        language_str = language_str + f"Reflection={self.reflection}, "
        language_str = language_str + f"First appeared in {self.year}"
        return language_str


# test code
if __name__ == "__main__":
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    print(python)

    # let's see if the is_dynamic method works
    is_python_dynamic = python.is_dynamic()
    print(f"Python is dynamic: {is_python_dynamic}")