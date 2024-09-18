#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for i in matrix:
        subArr = []
        for j in i:
            subArr.append(j ** 2)
        result.append(subArr)
    return (result)
