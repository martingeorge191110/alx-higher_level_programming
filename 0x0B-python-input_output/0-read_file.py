#!/usr/bin/python3

def read_file(filename=""):
    """Function to read file and print"""
    with open(filename, encoding="utf-8") as file
    for line in file:
        print(line, end="")
