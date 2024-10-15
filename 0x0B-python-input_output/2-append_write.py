#!/usr/bin/python3

"""append write module"""


def append_write(filename="", text=""):
    """Function to append and write file"""
    with open(filename, "a", encoding="utf-8") as file:
        length = file.write(text)
    return (length)
