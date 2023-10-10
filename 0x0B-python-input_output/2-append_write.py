#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    a function that appends a string to the end of a text file (UTF8) and returns the number of characters added.

    Args:
        filename (str): The name of the appended text file.
        text (str): The string to be added to the file.

    Returns:
        int: The number of characters added to the file.

    Raises:
	Exception as e if any error ocurs

    """
    try:
        with open(filename, 'a+', encoding='utf-8') as file:
            file.seek(0, 2)
            characters_added = file.write(text)
        return characters_added
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
