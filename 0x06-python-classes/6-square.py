#!/usr/bin/python3
"""Class With Attribute"""


class Square:
    """Square Class with size Attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize an Instance with size and postion Attributes"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieve size"""
        return (self.__size)

    @property
    def position(self):
        """Function to Retrieve Position"""
        return self.__position

    @size.setter
    def size(self, value):
        """Set new size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    @position.setter
    def position(self, value):
        """set new position Attribute"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
