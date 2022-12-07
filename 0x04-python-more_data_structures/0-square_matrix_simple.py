#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_new = [[x**2 for x in row] for row in matrix]
    return matrix_new
