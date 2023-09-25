#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x number of elememts of a list.
    Args:
        my_list (list): The list with elements.
        x (int): The number of elements for my_list to print.
    Returns:
        The number of elements printed.
    """
    element = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            element += 1
        except IndexError:
            break
    print("")
    return (element)
