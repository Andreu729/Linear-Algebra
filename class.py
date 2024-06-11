# Class and useful functions for it
def list_len(list_):  # length of list
    i = 0
    for value in list_:
        i += 1
    return i


def false_finder(value):
    if not value:
        print("Matrix error, not all rows are equal length")
        return True
    else:
        return False


false_finder([True, True, True, True])

def row_len(list_):  # length calculator used for rows
    all_lengths = []  # stores information of all row's lengths
    standard_len = list_len(list_[0])  # row length that every row should have
    for row in list_:
        equals = (list_len(row) == standard_len)
        all_lengths.append(equals)
    for b in all_lengths:
        t =


a = [[2, 3, 4], [4, 5, 6]]
print(list_len(a))


class Matrix:

    def __init__(self, matrix):  # constructor of matrix
        self.matrix = matrix
        self.row_amount = list_len(matrix)
