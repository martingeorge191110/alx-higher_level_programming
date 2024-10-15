#!/usr/bin/python3

def read_file(filename=""):
    """Function to read file and print"""
    file = open(filename, encoding="utf-8")
    print(file.read())
