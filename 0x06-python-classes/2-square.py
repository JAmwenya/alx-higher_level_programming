#!/usr/bin/python3

'''class that defines a square'''

class Square:
    '''structure of the Square'''

    def __init__(self, size=0):
        '''initialize the class Square.
        
        Args:
            size (int): The size of the new square.
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
