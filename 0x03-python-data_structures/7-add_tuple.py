#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tupleOne = tuple_a + (0, 0)
    tupleTwo = tuple_b + (0, 0)
    result = tupleOne[0] + tupleTwo[0], tupleOne[1] + tupleTwo[1]
    return (result)
