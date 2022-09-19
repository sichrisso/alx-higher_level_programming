#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [ele[:] for ele in matrix]
    for i in range(0, len(new_matrix)):
        for j in range(0, len(new_matrix[i])):
            new_matrix[i][j] = new_matrix[i][j] ** 2
    return new_matrix
