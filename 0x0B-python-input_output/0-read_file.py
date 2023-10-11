#!/usr/bin/python3
def read_file(filename=""):
    """
    This function reads a text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to be read with a default of an empty string.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
