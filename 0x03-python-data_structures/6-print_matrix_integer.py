#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(0,len(matrix)):
            l = len(matrix[i])
            for j in range(0,l):
                if j != (l-1):
                    print(matrix[i][j],end=" ")
                else:
                    print(matrix[i][j])
