#!/usr/bin/python3
"""A module with a function that writes a string to a file and counts the characters"""
def write_file(filename="", text=""):
    """This function writes a string to a text file (UTF8) and returns the number of characters written."""
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
