"""
CP1404/CP5632 Practical - Client code to use the ProgrammingLanguage class.
"""

from programming_language import ProgrammingLanguage


def main():
    """Main function to demo programming language functionality."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(visual_basic)

    # now let's put them in a list
    languages = [ruby, python, visual_basic]

    print("\nThe dynamically typed languages are:")
    # loop through and check each one if it's dynamic
    for language in languages:
        if language.is_dynamic() == True:
            print(language.name)

    # maybe I should add more languages later?
    # like javascript, c++, etc

    # alternative way using list comprehension - too advanced for me now
    # dynamic_languages = [language.name for language in languages if language.is_dynamic()]
    # print("\nDynamic languages using list comprehension:")
    # for language in dynamic_languages:
    #     print(language)

main()