#!/usr/bin/python3
def is_same_class(obj, a_class):

    """
    A function that checks if an object is exactly an instance of the specified class

    Args:
        obj: The object to check.
        a_class: The class to compare the object against.

    Returns:
        True if the object is an instance of the specified class, otherwise False.
    """

    obj_class = type(obj)

    return obj_class == a_class