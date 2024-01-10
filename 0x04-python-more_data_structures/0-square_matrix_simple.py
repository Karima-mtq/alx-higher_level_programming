#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    pow = lambda x: x**2
    new_mat=[]
    for row in matrix:
        new_mat.append(list(map(pow,row)))
    return new_mat
