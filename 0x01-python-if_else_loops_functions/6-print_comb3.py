#!/usr/bin/python3
for i in range(10):
    for k in range(10):
        if i == 8 and k == 9:
            print("{:d}{:d}".format(i, k))
            break
        if k > i and i < 8:
            print("{:d}{:d}".format(i, k), end=", ")
