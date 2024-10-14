#!/usr/bin/python3

"""add attribute module"""


def add_attribute(obj, attribute, value):
    """Function that add attributes to a class"""
    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
