#!/usr/bin/python3
"""Module with a function that appends a string to a file and counts the characters added"""

def append_write(filename="", text=""):
    """A function that appends a string to the end of a text file (UTF8) and returns the number of characters added."""
    with open(filename, 'a+', encoding='utf-8') as file:
        file.seek(0, 2)
        characters_added = file.write(text)
        return characters_added
