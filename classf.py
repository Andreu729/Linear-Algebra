# Class and useful functions for it
def list_len(list_):  # length of list
    i = 0
    for value in list_:
        i += 1
    return i


def col_len(list_):  # length calculator used for cols
    all_lengths = []  # stores information of all col's lengths
    standard_len = list_len(list_[0])  # length that every col should have
    for row in list_:
        equals = (list_len(row) == standard_len)  # True if r_n has same cols as r_1
        all_lengths.append(equals)
    if False in all_lengths:  # doesn't return the col length if list has some False data
        print("Matrix doesn't have the same dimension of columns")
        return False
    else:
        return standard_len


class Matrix:

    def __init__(self, matrix):  # constructor of matrix
        self.matrix = matrix
        self.row_amount = list_len(matrix)
        self.col_amount = col_len(matrix)
