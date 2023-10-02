#!usr/bin/python3
"""
module with one function that returns the sum of two arguments

"""
def add_integer(a, b=98):
    """
    adds two integers or floats and returns the sum.
    
    Args:
        a: first argument
        b: second argument with 98 as default.
    
    Return:
    	The sum of a and b.

    Raises:
    TypeError: If a or b is not an integer
    """
	if not (isinstance(a, int) or isinstance(a, float)):
		raise TypeError("a must be an integer or b must be an integer")
	if not (isinstance(b, int) or isinstance(b, float)):
		raise TypeError("a must be an integer or b must be an integer")
	return int(a + b)
