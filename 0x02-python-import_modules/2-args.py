#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argvLen = len(argv)
    if argvLen == 1:
        print("0 arguments.")
    elif argvLen == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(argvLen - 1))
        i = 1
        while i < argvLen:
           print("{}: {}".format(i, argv[i]))
           i += 1
