# Class and useful functions for it
def list_len(list_):  # length of list
    i = 0
    for value in list_:
        i += 1
    return i


def col_len(list_):  # length calculator used for cols
    is_same_length = []  # stores information of all col's lengths
    standard_len = list_len(list_[0])  # length that every col should have
    for row in list_:
        equals = (list_len(row) == standard_len)  # True if r_n has same cols as r_1
        is_same_length.append(equals)
    if False in is_same_length:  # doesn't return the col length if list has some False data
        print("Matrix doesn't have the same dimension of columns")
        return False
    else:
        return standard_len


def max_finder(matrix, n, v=0):
    str_value1 = str(matrix[v][n-1])  # Initial value of n-th column of matrix, made a string
    max_ = len(str_value1)  # length of initial value, and initial max_.
    is_max = []  # list of True or false bools
    for row in matrix:
        str_value2 = str(row[n-1])  # value of n-th column and i-th row
        bool_ = (len(str_value2) <= max_)  # False if there exists a length higher than our defined max_
        is_max.append(bool_)  # appends every result in bool_
    if False in is_max:
        return max_finder(matrix, n, v+1)  # if False repeats the function but with a different max_
    else:
        return max_  # return max_ when the highest length was found.


class Matrix:

    def __init__(self, matrix):  # constructor of matrix
        self.matrix = matrix
        self.row_amount = list_len(matrix)
        self.col_amount = col_len(matrix)
