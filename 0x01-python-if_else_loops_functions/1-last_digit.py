#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if (number < 0):
    lastDigit = ((number * -1) % 10) * -1
else:
    lastDigit = number % 10

print(f"Last digit of {number} is {lastDigit}", end=" ")

if lastDigit > 5:
    print("and is greater than 5")
elif lastDigit < 6 and lastDigit != 0:
    print("and is less than 6 and not 0")
else:
    print("and is 0")
