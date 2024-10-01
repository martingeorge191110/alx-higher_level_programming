#!/usr/bin/python3
"""Class With Attribute"""


class Square:
    """Square Class with size Attribute"""
    def __init__(self, size=0):
        """Initialize an Instance with size Attribute"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size

    @property
    def size(self):
        """Retrieve size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set new size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        """
        Function to Calc Area
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Print the squar using #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
