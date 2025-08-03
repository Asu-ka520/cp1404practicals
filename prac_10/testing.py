"""
CP1404/CP5632 - Practical
Testing demo using assert and doctest
"""

from car import Car

def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)

def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in

    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length

def phrase_to_sentence(phrase):
    """
    Convert phrase to a sentence with proper capitalization and a full stop.

    >>> phrase_to_sentence("hello world")
    'Hello world.'
    >>> phrase_to_sentence("hello world.")
    'Hello world.'
    >>> phrase_to_sentence("Hello world")
    'Hello world.'
    """
    phrase = phrase.strip()
    if not phrase.endswith('.'):
        phrase = phrase + '.'
    return phrase[0].upper() + phrase[1:]

def run_tests():
    """Run some tests on the Car class and others."""

    # assert test for repeat_string
    assert repeat_string("hi", 2) == "hi hi"
    assert repeat_string("bye", 3) == "bye bye bye"

    # assert tests for is_long_word
    assert is_long_word("Python")      # 6 >= 5，True
    assert not is_long_word("hi")      # 2 < 5，False
    assert is_long_word("Python", 6)   # 6 >= 6, True
    assert not is_long_word("hello", 6) # 5 < 6, False

    # assert tests for phrase_to_sentence
    assert phrase_to_sentence("hello") == "Hello."
    assert phrase_to_sentence("it is an apple") == "It is an apple."
    assert phrase_to_sentence("This is sentence.") == "This is sentence."
    assert phrase_to_sentence("  spaced out  ") == "Spaced out."

    # Testing Car class
    test_car = Car("Test", 10)
    assert test_car.name == "Test"
    assert test_car.fuel == 10
    test_car.add_fuel(5)
    assert test_car.fuel == 15
    test_car.drive(5)
    assert test_car.odometer == 5
    assert test_car.fuel == 10

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    run_tests()
    print("All tests passed.")