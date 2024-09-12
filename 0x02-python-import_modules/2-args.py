#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argvLen = len(argv)
    if argvLen == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(argvLen - 1))
    i = 1
    while i < argvLen:
        print("{} {}".format(i, argv[i]))
        i += 1
