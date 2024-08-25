import copy

from classf import *


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
    if col not in range(1, matrix.col_amount + 1) or last_pivot_row not in range(matrix.row_amount):
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


def row_reduce(matrix, *, set_option=0):  # returns matrix into it's reduced form
    #  options: 0 = returns matrix in reduced form, 1 = return total pivot amount, 2 = return free column positions
    matrix = Matrix(copy.deepcopy(matrix.matrix))
    pivot_row = 0
    pivot_amount = 0
    no_pivot_cols = []
    for col in range(1, matrix.col_amount + 1):
        matrix = single_row_reduce(matrix, col=col, last_pivot_row=pivot_row)
        if not pivot_find(matrix, col=col, last_pivot_row=pivot_row) == 0:
            pivot_row = pivot_find(matrix, col=col, last_pivot_row=pivot_row)
            pivot_amount += 1
        else:
            no_pivot_cols.append(col)
    if set_option == 1:
        return pivot_amount
    elif set_option == 2:
        return no_pivot_cols
    else:
        return matrix


def null_space(matrix):  # finds the nullspace of matrix
    if row_reduce(matrix, set_option=1) == matrix.col_amount:
        null_vector = []
        for zero in range(matrix.col_amount):
            null_vector.append(0)
        return null_vector
    free_col_list = row_reduce(matrix, set_option=2)
    reduced_matrix_t = transpose(row_reduce(matrix))
    null_space_list = []
    for col_number in range(1, matrix.col_amount + 1):
        if col_number in free_col_list:
            vector_generator = []
            free_col_amount = 0
            inverse_free_col = row_amplification(reduced_matrix_t, row=col_number, scalar=-1).matrix[col_number - 1]
            for other_free_cols_searcher in range(1, matrix.col_amount + 1):
                if other_free_cols_searcher == col_number:
                    vector_generator.append(1)
                    free_col_amount += 1
                elif other_free_cols_searcher in free_col_list:
                    vector_generator.append(0)
                    free_col_amount += 1
                else:
                    last_pivot = other_free_cols_searcher - free_col_amount
                    vector_generator.append(inverse_free_col[last_pivot - 1])
            null_space_list.append("gen" + str(vector_generator))
    return null_space_list


def get_column(matrix, *, position):
    column = []
    if not position <= matrix.col_amount:
        return column

    for row in matrix.matrix:
        column.append(row[position - 1])

    return column


def augment_matrix(matrix, *, b):  # adds the b vector to the matrix as a new column
    matrix = Matrix(copy.deepcopy(matrix.matrix))

    if not matrix.row_amount == list_len(b):
        return False

    augmented_matrix = []
    matrix_list = matrix.matrix
    for row, i in zip(matrix_list, range(0, matrix.row_amount)):
        row.append(b[i])
        augmented_matrix.append(row)
    return Matrix(augmented_matrix)


def is_generated(*, matrix, augmented_matrix):  # checks if reduced form of matrix can generate b column
    pivot_amount_1 = row_reduce(matrix, set_option=1)
    pivot_amount_2 = row_reduce(augmented_matrix, set_option=1)
    if pivot_amount_2 == pivot_amount_1:
        return True
    return False


def null_space_as_sum(nullspace):
    null_space_formatted = ""
    started = False
    for gen in nullspace:
        if started:
            null_space_formatted += " + "
        else:
            started = True
        null_space_formatted += gen
    return null_space_formatted


def linear_solve(matrix, *, b):  # solves the matrix equation Ax = b and returns x as a list.
    augmented_matrix = augment_matrix(matrix, b=b)  # returns False if b has no length = row_amount of matrix.
    nullspace = null_space(matrix)
    if not augmented_matrix:
        print("Linear_Solve error detected, length of b is not equal to the amount of rows in matrix")
        return

    augmented_reduced = row_reduce(augmented_matrix, set_option=0)  # obtaining b column when rows are reduced.

    col_dim = matrix.col_amount
    row_dim = matrix.row_amount
    reduced_b = get_column(augmented_reduced, position=col_dim + 1)
    is_not_zero_vector = isinstance(nullspace[0], str)
    was_generated = is_generated(matrix=matrix, augmented_matrix=augmented_matrix)  # detecting if b is generated
    is_squared = col_dim == row_dim
    if not was_generated:
        print("Inconsistent Matrix Equation, b is not generated by matrix")
        return
    elif not is_not_zero_vector and was_generated and is_squared:

        return reduced_b
    elif not is_not_zero_vector and was_generated:
        new_b = []
        for loop in range(0, col_dim):
            new_b.append(reduced_b[loop])

        return new_b
    else:
        new_b = []
        free_cols = row_reduce(matrix, set_option=2)
        a = 0
        for pos in range(1, col_dim + 1):
            if pos in free_cols:
                new_b.append(0)
            else:
                new_b.append(reduced_b[a])
                a += 1
        nullspace_sum = null_space_as_sum(nullspace)
        return str(new_b) + " + " + nullspace_sum
