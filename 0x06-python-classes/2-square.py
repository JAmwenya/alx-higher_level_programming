#!/usr/bin/python3

'''class that defines a square'''

class Square:
    '''structure of the Square'''

    def __init__(self, size=0):
        '''initialize the class Square.
        
        Args:
            size (int): The size of the new square.
        '''

    try: 
        type(size) = int
    except: TypeError:
        print('size must be an integer')
        break

    try:
        self.__size < 0 
    except: ValueError:
        print('size must be >= 0')
