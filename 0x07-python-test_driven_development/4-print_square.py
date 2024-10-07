#!/usr/bin/python3

def print_square(size):
    """Print square function (using #)

    Args:
       size (int): square size

    Raises:
       TypeError: if size is not integer
       ValueError: if size less than zero
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
