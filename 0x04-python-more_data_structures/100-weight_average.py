#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    s = 0
    q = 0
    for x in my_list:
        s += (x[0] * x[1])
        q += x[1]
    return s/q
