#!/usr/bin/python3

"""is same class module"""


def is_same_class(obj, a_class):
    """Function to chek whether obj is instance of class

    Args:
       obj: object
       a_class: class

    Return:
       True: if the object is instance of the class
       False: if not
    """
    if type(obj) is a_class:
        return (True)
    else:
        return (False)
