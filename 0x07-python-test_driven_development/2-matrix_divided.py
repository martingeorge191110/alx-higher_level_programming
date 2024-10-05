#!/usr/bin/python3

def matrix_divided(matrix, div):
    """Function divides all elements of a matrix.

    Args:
        matrix (list): matrix to devide
        div (int / float): devisor numebr

    Returns:
        new matrix which after devision

    Raises:
        TypeError: When matrix is not a list of lists of ints or floats.
        TypeError: When the rows of the matrix are not all the same length.
        TypeError: When div is not an numebr (integer / float).
        ZeroDivisionError: When div is 0.
    """
    result = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    matrixMsg1 = "matrix must be a matrix (list of lists) of integers/floats"
    matrixMsg2 = "Each row of the matrix must have the same size"
    if not isinstance(matrix, list) or len(matrix) < 2:
        raise TypeError(matrixMsg1)

    for i in matrix:
        if type(i) is not list:
            raise TypeError(matrixMsg1)

    stdLen = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) != stdLen:
            raise TypeError(matrixMsg2)
        for j in matrix[i]:
            if not isinstance(j, (int, float)):
                raise TypeError(matrixMsg1)
        result.append([round(j / div, 2) for j in matrix[i]])

    return (result)
