#!/usr/bin/python3

"""write file module"""


def write_file(filename="", text=""):
    """Function to write into file"""
    with open(filename, "w", encoding="utf-8") as file:
        length = file.write(text)
    return (length)
