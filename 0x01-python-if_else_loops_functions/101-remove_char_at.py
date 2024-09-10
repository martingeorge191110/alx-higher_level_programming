#!/usr/bin/python3
def remove_char_at(str, n):
    if (len(str) - 1 < n or n < 0):
        return str

    newStr = ""
    for i in str:
        if i == str[n]:
            continue

        newStr += i

    return newStr
