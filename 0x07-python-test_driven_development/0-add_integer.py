#!/usr/bin/python3

def add_integer(a, b=98):
    """Function to add integers

    Args:
         a (int): first integer
         b (int): second integer

    Returns:
         int: sum of a and b

    Raises:
        TypeError: if a or b is not an integer or float
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
