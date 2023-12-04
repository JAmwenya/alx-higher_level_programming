#!/usr/bin/python3
"""Class that inherits from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle that inherits from a base class"""

    def __init__(self, width, height):
        """Initialize a new rectangle
        """
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height

    def area(self):
        """Defines the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the print() and str() representation of a rectangle"""
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "/" + str(self.__height)
        return string
