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


def str_adder(list_, string):
    new_list = []
    for value in list_:
        value = value + string
        new_list.append(value)
    return new_list


def adder_looper(value, string, times):
    for a in range(times):
        value += string
    return value


def control_add(value, string, happens=True):
    if not happens:
        return value
    else:
        return value + string


def visual_constructor(matrix, n):
    start = ""
    constructed = []
    final = False
    if n == 1:
        start = "[ "
    elif n == matrix.col_amount:
        final = True
    k = max_finder(matrix.matrix, n)
    for row in matrix.matrix:
        m = len(str(row[n - 1]))
        value = adder_looper(start, " ", k - m + 1)
        visual = value + str(row[n - 1])
        visual = control_add(visual, " ]", final)
        constructed.append(visual)
    return constructed


def list_union(list1, list2):
    l1 = list_len(list1)
    l2 = list_len(list2)
    union_list = []
    if not l1 == l2:
        return union_list
    for n in range(l1):
        string = list1[n] + list2[n]
        union_list.append(string)
    return union_list


def visual_final(matrix):
    print_list = visual_constructor(matrix, 1)
    for n in range(2, matrix.col_amount + 1):
        construction = visual_constructor(matrix, n)
        print_list = list_union(print_list, construction)
    return print_list


def list_print(list_):
    for value in list_:
        print(value)


class Matrix:

    def __init__(self, matrix):  # constructor of matrix
        self.matrix = matrix
        self.row_amount = list_len(matrix)
        self.col_amount = col_len(matrix)
        self.matrix_form = visual_final(self)

    def mprint(self):
        matrix_list = self.matrix_form
        list_print(matrix_list)
