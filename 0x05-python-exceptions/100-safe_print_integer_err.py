#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}\n".format(value))
        return (True)
    except (TypeError, ValueError) as error:
        sys.stdout.write("Exception: {}\n".format(error))
        return (False)
