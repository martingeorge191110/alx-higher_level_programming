#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cpyList = my_list.copy()
    for i in range(len(cpyList)):
        if cpyList[i] == search:
            cpyList[i] = replace
    return (cpyList)
