#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for x in list(a_dictionary):
        a_dictionary[x] *= 2
    return a_dictionary
