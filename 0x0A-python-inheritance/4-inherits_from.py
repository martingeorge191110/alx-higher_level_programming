#!/usr/bin/python3

"""inherits form module"""


def inherits_from(obj, a_class):
    """Function to returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class
    
    Args:
       obj: object
       a_class: class
    
    Return:
       True: if instance
       False: otherwise
    """
    if type(obj) is a_class:
        return (False)
    else:
        return (isinstance(obj, a_class))
