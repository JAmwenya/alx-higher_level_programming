#!/usr/bin/python3
"""Returns the list of available attributes and methods of an object"""

class InpectObject:
    """
    A class that lists available attribute and methods of an object.

    Usage:
   Create a class instance.
   Call the `lookup(obj)` method with the object you want to inspect.

    """
def lookup(self, obj):
        """
        Lists available attributes and methods of an object.

        Args:
        obj: The object to be inspected.

        Returns:
       	A list of attribute and method names.
        """
        return dir(obj)
