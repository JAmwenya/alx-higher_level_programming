#!/usr/bin/python3
"""
    Module that returns the list of available attributes and methods of an object
"""


def lookup(obj):
        """
        A function that returns the list of available attributes and methods of an object.

        Args:
        obj: The object to be inspected.

        Returns:
       	A list of all available attribute and method names.
        """
        return dir(obj)
