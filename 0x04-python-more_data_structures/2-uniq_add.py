#!/usr/bin/python3
def uniq_add(my_list=[]):
    setList = {0}
    sum = 0
    for i in my_list:
        setList.add(i)
    for i in setList:
        sum += i
    return (sum)
