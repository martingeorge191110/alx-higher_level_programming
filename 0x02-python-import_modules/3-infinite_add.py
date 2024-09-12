#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argvLen = len(argv)
    if argvLen == 1:
        print("{}".format(0))
    elif argvLen == 2:
        print("{}".format(argv[1]))
    else:
        sum, i = 0, 1
        while i < argvLen:
            sum += int(argv[i])
            i += 1
        print("{}".format(sum))
