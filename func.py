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


def row_amplification(matrix, *, row, scalar):  # multiplies the row of the matrix by an n factor
    matrix = matrix.matrix
    new_row = []
    for value in matrix[row - 1]:
        value = value * scalar
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


def row_operation(matrix, *, changed_row, scalar, changer_row):  # row operation, row_1 -> row_1 + n * row_2
    matrix_ = matrix.matrix
    number = changed_row
    changed_row = matrix_[changed_row - 1]
    changer_row = matrix_[changer_row - 1]
    new_row = []
    for i in range(matrix.col_amount):
        value = changed_row[i] + changer_row[i] * scalar
        new_row.append(value)
    matrix_[number - 1] = new_row
    return Matrix(matrix_)


def pivot_find(matrix, *, col, last_pivot_row):  # searches for a pivot value in the col
    if not col in range(1, matrix.col_amount + 1) or not last_pivot_row in range(matrix.row_amount):
        return 0
    matrix_list = matrix.matrix
    if not matrix_list[last_pivot_row][col - 1] == 0:
        return last_pivot_row + 1
    else:
        return pivot_find(matrix, col=col, last_pivot_row=last_pivot_row + 1)


def single_row_reduce(matrix, *, col, last_pivot_row):  # reduces one single column of matrix and returns it.
    matrix_list = matrix.matrix
    actual_pivot_pos = pivot_find(matrix, col=col, last_pivot_row=last_pivot_row)
    if actual_pivot_pos == 0:
        return matrix
    elif not actual_pivot_pos - last_pivot_row == 1:
        matrix = row_permutation(matrix, last_pivot_row + 1, actual_pivot_pos)
        actual_pivot_pos = last_pivot_row + 1

    pivot_value = matrix_list[actual_pivot_pos - 1][col - 1]
    matrix = row_amplification(matrix, row=actual_pivot_pos, scalar=1 / pivot_value)  # changes pivot to 1
    for row in range(matrix.row_amount):
        if not row == actual_pivot_pos - 1:
            component_value = matrix_list[row][col - 1]
            matrix = row_operation(matrix, changed_row=row + 1, scalar=-component_value, changer_row=actual_pivot_pos)
    return matrix


def row_reduce(matrix):  # returns matrix into it's reduced form
    pivot_row = 0
    for col in range(1, matrix.col_amount + 1):
        matrix = single_row_reduce(matrix, col=col, last_pivot_row=pivot_row)
        if not pivot_find(matrix, col=col, last_pivot_row=pivot_row) == 0:
            pivot_row = pivot_find(matrix, col=col, last_pivot_row=pivot_row)
    return matrix
