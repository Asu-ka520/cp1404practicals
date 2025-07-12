"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""

class ProgrammingLanguage:
    """Contains info about a programming language, including pointer arithmetic support."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """
        Initialize a ProgrammingLanguage instance.

        Arguments:
            name (str): Name of the language.
            typing (str): 'Static' or 'Dynamic'.
            reflection (bool): Whether it supports reflection.
            year (int): Release year.
            pointer_arithmetic (bool): Whether it supports pointer arithmetic.
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __repr__(self):
        """Return a clear, detailed string for debugging."""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"Pointer Arithmetic={self.pointer_arithmetic}, First appeared in {self.year}")

    def __str__(self):
        """Return a nicely formatted description."""
        reflection_str = "has" if self.reflection else "no"
        pa_str = "supports" if self.pointer_arithmetic else "does not support"
        return (f"{self.name} ({self.year}): {self.typing} typing, "
                f"{reflection_str} reflection, {pa_str} pointer arithmetic")

    def is_dynamic(self):
        """Returns True if the language is dynamically typed."""
        return self.typing.lower() == "dynamic"