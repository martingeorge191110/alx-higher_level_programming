#!/usr/bin/python3
def uppercase(str):
    for i in str:
        character = i
        if ord(i) >= 97 and ord(i) <= 122:
            character = chr(ord(i) - 32)
        print("{}".format(character), end="")
    print("")
