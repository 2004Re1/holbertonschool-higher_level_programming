#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix by squaring each element in the original matrix
    new_matrix = [[element ** 2 for element in row] for row in matrix]
    return new_matrix
