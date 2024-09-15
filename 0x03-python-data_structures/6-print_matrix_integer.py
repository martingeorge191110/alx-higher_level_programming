#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        for element in arr:
            if element != arr[-1]:
                print("{:d}".format(element), end=" ")
            else:
                print("{:d}".format(element))
