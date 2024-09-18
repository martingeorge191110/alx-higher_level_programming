#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    romNumbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                  'M': 1000}
    sum = 0
    for i in range(len(roman_string)):
        result = romNumbers[roman_string[i]]
        if len(roman_string) <= (i + 1):
            sum += result
        else:
            if result < romNumbers[roman_string[i + 1]]:
                sum -= result
            else:
                sum += result
    return (sum)
