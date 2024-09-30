#!/usr/bin/python3
def magic_calculation(a, b):
    finalResult = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            finalResult = finalResult + ((a ** b) / i)
        except Exception:
            finalResult = b + a
            break
    return (finalResult)
