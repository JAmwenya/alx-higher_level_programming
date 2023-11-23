#!usr/bin/python3
"""
module with one function that divides all elements of a matrix

"""
def matrix_divided(matrix, div):
    """
    divides the first agument by the second
    
    Args:
        matrix: first argument that is divided by the second argument
        div: second argument that divides each element of the first argument
    
    Return:
        new_matrix: result of first argument elements divided by the second argument

    Raises:
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    TypeError: Each row of the matrix must have the same size
    TypeError: div must be a number
    ZeroDivisionError: division by zero
    """
    if not (isinstance(row, list) and (isinstance(objct, (int, float)) for objct in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = set(len(row) for row in matrix)
    if len(row_size) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
	raise TypeError("div must be a number")
    if div == 0:
	raise ZeroDivisionError("division by zero")
 
new_matrix = []
    for row in matrix:
        new_row = [round(objct / div, 2) for objct in row]
        new_matrix.append(new_row)
    
    return new_matrix
