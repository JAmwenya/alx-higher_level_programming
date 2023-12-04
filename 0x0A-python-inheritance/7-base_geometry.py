#!/usr/bin/python3
"""Defines a class BaseGeometry"""

class BaseGeometry:
    """Represents a base geometry class"""
    
    def area(self):
        """Does not implement the method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value an an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{}must be greater than 0".format(name))
