#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for ls in sorted(a_dictionary):
        print(ls,": ",a_dictionary[ls],sep="")
