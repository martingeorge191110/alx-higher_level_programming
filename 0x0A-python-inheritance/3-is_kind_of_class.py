#!/usr/bin/python3

"""is kind of class module"""


def is_kind_of_class(obj, a_class):
    """Function to check whether obj is instance of a_class

    Args:
        obj: object
        a_class: class

    Return:
        True: True if the object is an instance of a_class
        False: otherwise
    """
    return (isinstance(obj, a_class))
