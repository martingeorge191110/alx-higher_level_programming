#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """Rectangle Class"""

    number_of_instances = 0
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

    def __str__(self):
        result = ""
        if self.__width == 0 or self.__height == 0:
            return ("")

        for i in range(self.__height):
            for j in range(self.__width):
                result += "#"
            if i < self.__height - 1:
                result += '\n'
        return (result)

    @property
    def width(self):
        """Function to retrieve width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Function to set width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print(f"Bye rectangle...")

    @property
    def height(self):
        """Function to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """function to set new height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Function to retrieve area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Function to retrieve perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)

        return ((self.__width + self.__height) * 2)
