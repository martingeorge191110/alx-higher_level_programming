#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    length = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            length += 1
        except (TypeError, ValueError):
            pass
    print()
    return (length)
