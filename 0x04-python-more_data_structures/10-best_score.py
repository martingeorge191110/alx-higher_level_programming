#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)

    biggest = list(a_dictionary.keys())[0]
    for key in a_dictionary:
        if a_dictionary[key] > a_dictionary[biggest]:
            biggest = key

    return (biggest)
