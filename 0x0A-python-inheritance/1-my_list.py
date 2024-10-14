#!/usr/bin/python3

"""MyList module"""


class MyList(list):
    """Class which inherets from list"""
    def print_sorted(self):
        """Function that prints sorted list"""
        cpyList = self.copy()
        cpyList.sort()
        print(cpyList)
