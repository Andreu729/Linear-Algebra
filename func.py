from classf import *


def linear_solve(matrix, b):  # solves the matrix equation Ax = b and returns x as a list.
    pass  # first a row reduce function is needed


def column_extend(matrix, b):  # extends the og matrix introducing the new b column.
    if not matrix.row_amount == list_len(b):
        return matrix
    new_matrix = []
    i = 0
    for row in matrix.matrix:
        row.append(b[i])
        new_matrix.append(row)
        i += 1
    return Matrix(new_matrix)
