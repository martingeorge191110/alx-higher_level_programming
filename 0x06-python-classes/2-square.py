#!/usr/bin/python3
"""Class With Attribute"""


class Square:
    """Square Class with size Attribute"""
    def __init__(self, size=0):
        """Initialize an Instance with size Attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size
