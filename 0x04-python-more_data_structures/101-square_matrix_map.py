#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda i: list(map(lambda ele: ele * ele, i)), matrix)))
