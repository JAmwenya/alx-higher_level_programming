#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    This function writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str): The destination text file.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.
    
    Raises:
	Exception as e if any errors occur
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            characters_written = file.write(text)
        return characters_written
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0
