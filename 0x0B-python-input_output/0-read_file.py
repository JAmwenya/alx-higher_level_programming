#!/usr/bin/python3
"""This module defines a function that reads text files"""


def read_file(filename=""):
    """This function reads a text file and prints its contents to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
