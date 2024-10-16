#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """Function that prints name

    Args:
        first_name (str): first name
        last_name (str): last name

    Raises:
         TypeError: when first_name or last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
