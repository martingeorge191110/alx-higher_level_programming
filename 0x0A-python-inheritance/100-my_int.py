#!/usr/bin/python3

"""my int module"""


class MyInt(int):
    """MyInt class"""

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return int(self.value) != int(other)

    def __ne__(self, other):
        return int(self.value) == int(other)
