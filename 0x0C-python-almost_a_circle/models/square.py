#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """get square size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set new size"""
        self.width = value
        self.height = value

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
            "size": self.size,
            "x": self.x,
            "y": self.y
            }
        return (resDec)
