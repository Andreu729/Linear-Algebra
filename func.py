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


def single_reduce(matrix, n):  # reduces one single column of matrix and returns it as the same.
    pass


def row_amplification(matrix, row, n):  # multiplies the row of the matrix by an n factor
    matrix = matrix.matrix
    new_row = []
    for value in matrix[row - 1]:
        value = value * n
        new_row.append(value)
    matrix[row - 1] = new_row
    return Matrix(matrix)


def row_permutation(matrix, row_1, row_2):  # changes positions between row_1 and row_2
    matrix = matrix.matrix
    first_row = matrix[row_1 - 1]
    second_row = matrix[row_2 - 1]
    matrix[row_1 - 1] = second_row
    matrix[row_2 - 1] = first_row
    return Matrix(matrix)


def row_operation(matrix, row_1, row_2, n):  # row operation, row_1 -> row_1 + n * row_2
    matrix_ = matrix.matrix
    number = row_1
    row_1 = matrix_[row_1 - 1]
    row_2 = matrix_[row_2 - 1]
    new_row = []
    for i in range(matrix.col_amount):
        value = row_1[i] + row_2[i] * n
        new_row.append(value)
    matrix_[number - 1] = new_row
    return Matrix(matrix_)
