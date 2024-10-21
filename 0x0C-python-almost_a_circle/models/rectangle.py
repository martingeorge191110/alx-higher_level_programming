#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Function that display instance in string format"""
        id = self.id
        width = self.width
        height = self.height
        x = self.x
        y = self.y
        return f"[Rectangle] ({id}) {x}/{y} - {width}/{height}"

    @property
    def width(self):
        """get width"""
        return (self.width)

    @width.setter
    def width(self, width):
        """set new width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be bigger than 0")
        self.__width = width

    @property
    def height(self):
        """get height"""
        return (self.__height)

    @height.setter
    def height(self, height):
        """set new height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be bigger then 0")
        self.__height = height

    @property
    def x(self):
        """get x"""
        return (self.__x)

    @x.setter
    def x(self, x):
        """set new x value"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Function to returns the area value"""
        return (self.width * self.height)

    def display(self):
        """Function to print in stdout
        the Rectangle instance with the character # by taking
        y and also x"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except Exception:
            pass
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Function that returns
        the dictionary representation"""
        resDec = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
            }
        return (resDec)
