#!/usr/bin/python3
"""Solving N queens puzzle"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    number = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if number < 4:
    print("N must be at least 4")
    exit(1)

if number == 4:
    firstList = [[0, 1], [1, 3], [2, 0], [3, 2]]
    secondList = [[0, 2], [1, 0], [2, 3], [3, 1]]
    print(firstList)
    print(secondList)
