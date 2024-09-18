#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDic = {}
    for key in a_dictionary:
        newDic[key] = newDic[key] * 2
    return (newDic)
