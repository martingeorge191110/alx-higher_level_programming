#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    length = 0
    for length in range(x):
        try:
            print("{:d}".format(my_list[length]), end='')
            length += 1
        except TypeError:
            length -= 1
            pass
        except ValueError:
            length -= 1
            pass
    print()
    return (length)
