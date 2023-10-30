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
        self.integer_validator("height", heigt)
        self.height = height
