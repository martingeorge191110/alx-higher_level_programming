#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpied_list = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return (cpied_list)
    cpied_list[idx] = element
    return (cpied_list)
