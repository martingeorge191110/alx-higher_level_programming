#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""
    myList = list_of_integers

    if myList == []:
        return (None)

    temp = myList[0]
    for i in range(0, len(myList) - 1):
        if myList[i] >= myList[i + 1]:
            temp = myList[i + 1]
            myList[i + 1] = myList[i]
            myList[i] = temp

    return myList[-1]

